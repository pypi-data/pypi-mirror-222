from google.cloud import ndb

# from src.client import fetch_article
from news_toolkit_api.src.models.article import Article
from news_toolkit_api.src.utils import sha3_256_hash


async def background_task_article(
    client: ndb.Client, article_id: str, fetch_related_article: bool = True
):
    article = None
    # await fetch_article(article_id)
    if not article:
        return None

    with client.context():
        article.key = ndb.Key(Article, sha3_256_hash(article.article_id))
        article.put()

    if fetch_related_article:
        for related_article in article.related_articles:
            await background_task_article(client, related_article.article_id, False)

    return article
