from fastapi import APIRouter, BackgroundTasks, Depends
from google.cloud import ndb
from fastapi_injector import Injected
from news_toolkit_api.api.v1.db import get_client
from news_toolkit_api.api.v1.response import (
    ArticleResponse,
    CategoriesResponse,
    SubscriptionCost,
    SubscriptionResponse,
    SubscriptionsResponse,
)
from news_toolkit_api.src.repository.article import ArticleRepository
from news_toolkit_api.src.background_tasks.article import background_task_article
from news_toolkit_api.src.models import Article, Category, Subscription
from news_toolkit_api.src.news_blocks import (
    ArticleIntroductionBlock,
    BannerAdContent,
    BannerAdSize,
    TextLeadParagraphBlock,
)
from news_toolkit_api.src.utils import needs_update, sha3_256_hash

router = APIRouter(prefix="/api/v1")


@router.get("/articles/{article_id}")
async def get_article(
    article_id: str,
    background_tasks: BackgroundTasks,
    limit: int = 20,
    offset: int = 0,
    client: ndb.Client = Depends(get_client),
    article_repository: ArticleRepository = Injected(ArticleRepository),
):
    with client.context():
        article: Article = ndb.Key(Article, sha3_256_hash(article_id)).get()

    if not article:
        article = await background_task_article(
            client, article_repository, article_id, True
        )
        if not article:
            return {}

    if needs_update(article.created_at):
        background_tasks.add_task(
            background_task_article, client, article_repository, article_id, True
        )

    contents = [
        ArticleIntroductionBlock(
            title=article.title,
            category=article.category,
            image_url=article.image_url,
            author=article.auther,
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
