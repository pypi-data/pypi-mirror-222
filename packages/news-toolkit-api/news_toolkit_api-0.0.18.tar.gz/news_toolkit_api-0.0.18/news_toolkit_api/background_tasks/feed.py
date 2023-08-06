from google.cloud import ndb

from news_toolkit_api.background_tasks.article import background_task_article
from news_toolkit_api.db import Category, Feed
from news_toolkit_api.repository import ArticleRepository, FeedRepository
from news_toolkit_api.utils import needs_update, sha3_256_hash


async def background_task_feed(
    client: ndb.Client,
    article_repository: ArticleRepository,
    feed_repository: FeedRepository,
    category: str,
):
    with client.context():
        latest: Feed | None = Feed.query().order("-created_at").get()
        if latest and not needs_update(latest.created_at):
            return

    feeds = await feed_repository.fetch_content(category)
    if not feeds:
        return None

    with client.context():
        for feed in feeds:
            feed.key = ndb.Key(
                Category, sha3_256_hash(category), Feed, sha3_256_hash(feed.article_id)
            )
        ndb.put_multi(feeds)

    for feed in feeds:
        await background_task_article(client, article_repository, feed.article_id, 0)
    return feeds
