from dataclasses import dataclass

from news_toolkit_api.src.news_blocks import (
    ArticleIntroductionBlock,
    BannerAdContent,
    TextLeadParagraphBlock,
)


@dataclass(frozen=True)
class ArticleResponse:
    title: str
    content: list[ArticleIntroductionBlock | TextLeadParagraphBlock | BannerAdContent]
    url: str
    is_premium: bool
    is_preview: bool
    total_count: int
