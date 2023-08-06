from google.cloud import ndb

from news_toolkit_api.config.settings import NEWS_TOOLKIT_MAX_RECURSION_DEPTH
from news_toolkit_api.db.article import Article
from news_toolkit_api.repository.article import ArticleRepository
from news_toolkit_api.utils import sha3_256_hash


async def background_task_article(
    client: ndb.Client,
    article_repository: ArticleRepository,
    article_id: str,
    depth: int = 0,
):
    article, _ = await article_repository.fetch_content(article_id)
    if not article:
        return None

    with client.context():
        article.key = ndb.Key(Article, sha3_256_hash(article.article_id))
        article.put()

    if depth < NEWS_TOOLKIT_MAX_RECURSION_DEPTH:
        for related_article in article.related_articles:
            await background_task_article(
                client, article_repository, related_article.article_id, depth + 1
            )

    return article
