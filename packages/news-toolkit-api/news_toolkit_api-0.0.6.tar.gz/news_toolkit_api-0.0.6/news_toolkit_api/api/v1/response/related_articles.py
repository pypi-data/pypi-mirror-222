from dataclasses import dataclass
from datetime import datetime
from enum import Enum


@dataclass(frozen=True)
class NavigateToArticleAction:
    article_id: str
    __identifier = "__navigate_to_article__"

    def type(self) -> str:
        return self.__identifier


class BlockType(Enum):
    post_small = "__post_small__"


@dataclass(frozen=True)
class RelatedArticleResponse:
    id: str
    title: str
    category: str
    image_url: str
    author: str | None
    published_at: datetime | None
    is_premium: bool
    type: BlockType
    action: NavigateToArticleAction


@dataclass(frozen=True)
class RelatedArticlesResponse:
    related_articles: list[RelatedArticleResponse]
    total_count: int
