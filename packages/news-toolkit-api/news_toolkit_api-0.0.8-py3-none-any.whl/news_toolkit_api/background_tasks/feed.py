from google.cloud import ndb

from news_toolkit_api.background_tasks.article import background_task_article
from news_toolkit_api.db import Category, Feed
from news_toolkit_api.repository.article import ArticleRepository
from news_toolkit_api.utils import needs_update, sha3_256_hash


async def background_task_feed(
    client: ndb.Client,
    article_repository: ArticleRepository,
    category: str,
):
    with client.context():
        latest: Feed | None = Feed.query().order("created_at").get()
        if latest and not needs_update(latest.created_at):
            return

    feeds = await article_repository.fetch_feed(category)
    if not feeds:
        return None

    with client.context():
        for feed in feeds:
            feed.key = ndb.Key(Feed, sha3_256_hash(feed.article_id))
            feed.parent = ndb.Key(Category, sha3_256_hash(category))
        ndb.put_multi(feeds)

    for feed in feeds:
        await background_task_article(client, article_repository, feed.article_id, True)
    return feeds
