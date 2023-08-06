from fastapi import APIRouter, BackgroundTasks, Depends
from google.cloud import ndb

from news_toolkit_api.api.v1.db import get_client
from news_toolkit_api.api.v1.injected import injected
from news_toolkit_api.api.v1.response import (
    ArticleResponse,
    CategoriesResponse,
    ContentType,
    FeedResponse,
    FeedsResponse,
    FeedType,
    RelatedArticleResponse,
    RelatedArticlesResponse,
    SubscriptionCost,
    SubscriptionResponse,
    SubscriptionsResponse,
)
from news_toolkit_api.background_tasks.article import background_task_article
from news_toolkit_api.background_tasks.feed import background_task_feed
from news_toolkit_api.db import Article, Category, Feed, Subscription
from news_toolkit_api.news_blocks import (
    ArticleIntroductionBlock,
    BannerAdContent,
    BannerAdSize,
    BlockType,
    NavigateToArticleAction,
    SectionHeaderBlock,
    TextLeadParagraphBlock,
)
from news_toolkit_api.repository import ArticleRepository, FeedRepository
from news_toolkit_api.utils import needs_update, sha3_256_hash

router = APIRouter(prefix="/api/v1")


@router.get("/articles/{article_id}")
async def get_article(
    article_id: str,
    background_tasks: BackgroundTasks,
    limit: int = 20,
    offset: int = 0,
    client: ndb.Client = Depends(get_client),
    article_repository: ArticleRepository = injected(ArticleRepository),
):
    with client.context():
        article: Article | None = ndb.Key(Article, sha3_256_hash(article_id)).get()

    if not article:
        article = await background_task_article(
            client, article_repository, article_id, 0
        )
        if not article:
            return {}

    if needs_update(article.created_at):
        background_tasks.add_task(
            background_task_article, client, article_repository, article_id, 0
        )

    contents: ContentType = [
        ArticleIntroductionBlock(
            title=article.title,
            category=article.category,
            image_url=article.image_url,
            author=article.author,
            published_at=article.published_at,
            is_premium=False,
        )
    ]
    for content in article.content:
        match content:
            case "ADVERTISEMENT":
                contents.append(BannerAdContent(size=BannerAdSize.large))
            case _:
                contents.append(TextLeadParagraphBlock(text=content))

    return ArticleResponse(
        title=article.title,
        content=contents[offset : offset + limit],
        url=article.url,
        is_premium=article.is_premium,
        is_preview=article.is_preview,
        total_count=len(article.content),
    )


@router.get("/articles/{article_id}/related")
async def get_related_articles(
    article_id: str,
    background_tasks: BackgroundTasks,
    limit: int = 20,
    offset: int = 0,
    client: ndb.Client = Depends(get_client),
    article_repository: ArticleRepository = injected(ArticleRepository),
):
    with client.context():
        article: Article | None = ndb.Key(Article, sha3_256_hash(article_id)).get()

    if not article or needs_update(article.created_at):
        background_tasks.add_task(
            background_task_article, client, article_repository, article_id, 0
        )
        return RelatedArticlesResponse(related_articles=[], total_count=0)

    related_articles = []
    for related_article in article.related_articles[offset : offset + limit]:
        related_articles.append(
            RelatedArticleResponse(
                id=related_article.article_id,
                title=related_article.title,
                category=related_article.category,
                image_url=related_article.image_url,
                author=related_article.author,
                published_at=related_article.published_at,
                is_premium=False,
                type=BlockType.post_small,
                action=NavigateToArticleAction(
                    article_id=related_article.article_id,
                ),
            )
        )
    return RelatedArticlesResponse(
        related_articles=related_articles,
        total_count=len(article.related_articles),
    )


@router.get("/feed")
async def get_feed(
    category: str,
    background_tasks: BackgroundTasks,
    limit: int = 20,
    offset: int = 0,
    client: ndb.Client = Depends(get_client),
    article_repository: ArticleRepository = injected(ArticleRepository),
    feed_repository: FeedRepository = injected(FeedRepository),
):
    with client.context():
        if not ndb.Key(Category, sha3_256_hash(category)).get():
            return FeedsResponse(feed=[], total_count=0)

    feeds: FeedType = []
    if offset == 0:
        feeds.append(SectionHeaderBlock(title="新着記事"))
    with client.context():
        query = Feed.query().order("-published_at")
        # Aggregate total count
        total_count = query.count()
        for feed in query.fetch(limit=limit, offset=offset):
            feeds.append(
                FeedResponse(
                    id=feed.key.id(),
                    title=feed.title,
                    category=feed.category,
                    image_url=feed.image_url,
                    author=feed.author,
                    published_at=feed.published_at,
                    is_premium=False,
                    type=BlockType.post_large,
                    action=NavigateToArticleAction(
                        article_id=feed.article_id,
                    ),
                )
            )

    background_tasks.add_task(
        background_task_feed, client, article_repository, feed_repository, category
    )
    return FeedsResponse(feed=feeds, total_count=total_count)


@router.get("/subscriptions")
async def get_subscriptions(client: ndb.Client = Depends(get_client)):
    with client.context():
        subscriptions = []
        for subscription in Subscription.query():
            subscriptions.append(
                SubscriptionResponse(
                    id=subscription.key.id(),
                    name=subscription.name,
                    benefits=subscription.benefits,
                    cost=SubscriptionCost(
                        monthly=subscription.cost.monthly,
                        annual=subscription.cost.annual,
                    ),
                )
            )

    return SubscriptionsResponse(subscriptions=subscriptions)


@router.get("/categories")
async def get_categories(client: ndb.Client = Depends(get_client)):
    with client.context():
        categories = [category.name for category in Category.query()]

    return CategoriesResponse(categories=categories)


# fake endpoints


@router.get("/search/popular")
async def get_search_popular():
    return {
        "articles": [
            {
                "id": "5c47495a-608b-4e8b-a7f0-642a02594888",
                "category": "news",
                "author": "CNN",
                "published_at": "2022-03-17T00:00:00.000",
                "image_url": "https://scitechdaily.com/images/Ear-Hearing-Concept.jpg",
                "title": "Boeing makes third attempt to launch its Starliner capsule to the ISS",
                "description": "Boeing will try yet again Thursday to send the capsule it...",
                "is_premium": False,
                "type": "__post_small__",
            }
        ],
        "topics": [],
    }


@router.get("/search/relevant")
async def get_search_relevant():
    return {
        "articles": [
            {
                "id": "b1fc2ffc-eb02-42ce-af65-79702172a987",
                "category": "news",
                "author": "Northwestern University",
                "published_at": "2022-03-11T00:00:00.000",
                "image_url": "https://scitechdaily.com/images/Ear-Hearing-Concept.jpg",
                "title": "Restoring Hearing: New Tool To Create Ear Hair Cells Lost Due to Aging or Noise",
                "description": "‘We have overcome a major hurdle’ to restore hearing,...",
                "is_premium": False,
                "type": "__post_small__",
            }
        ],
        "topics": [],
    }


@router.get("/users/me")
async def get_me():
    return {
        "user": {
            "id": "2e99887d-d672-4b96-ad6a-123c1c7fa3fa",
            "subscription_plan": "premium",
        }
    }
