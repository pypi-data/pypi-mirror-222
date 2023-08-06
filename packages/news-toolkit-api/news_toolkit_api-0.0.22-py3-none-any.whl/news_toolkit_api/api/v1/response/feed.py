from dataclasses import dataclass
from datetime import datetime

from news_toolkit_api.news_blocks import (
    BlockType,
    NavigateToArticleAction,
    SectionHeaderBlock,
)


@dataclass(frozen=True)
class FeedResponse:
    id: str
    title: str
    category: str
    image_url: str
    author: str | None
    published_at: datetime | None
    is_premium: bool
    type: BlockType
    action: NavigateToArticleAction


FeedType = list[SectionHeaderBlock | FeedResponse]


@dataclass(frozen=True)
class FeedsResponse:
    feed: FeedType
    total_count: int
