from abc import ABCMeta, abstractmethod
from datetime import datetime

from bs4 import BeautifulSoup

from news_toolkit_api.client import fetch_content
from news_toolkit_api.db import Article, RelatedArticle


class ArticleRepository(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.html_text: str | None = None
        self.soup: BeautifulSoup | None = None

    @abstractmethod
    def build_url(self, article_id: str) -> str:
        pass

    @abstractmethod
    def parse_title(self) -> str | None:
        pass

    @abstractmethod
    def parse_content(self) -> list[str] | None:
        pass

    @abstractmethod
    def parse_category(self) -> str | None:
        pass

    @abstractmethod
    def parse_image_url(self) -> str | None:
        pass

    @abstractmethod
    def parse_auther(self) -> str | None:
        pass

    @abstractmethod
    def parse_published_at(self) -> datetime | None:
        pass

    @abstractmethod
    def parse_related_articles(self) -> list[RelatedArticle]:
        pass

    async def fetch_content(self, article_id: str) -> Article | None:
        article_url = self.build_url(article_id)
        self.html_text = await fetch_content(article_url)
        if not self.html_text:
            return None

        self.soup = BeautifulSoup(self.html_text, features="html5lib")
        if not self.soup:
            return None

        title = self.parse_title()
        content = self.parse_content()
        category = self.parse_category()
        if not title or not content or not category:
            return None

        return Article(
            article_id=article_id,
            title=title,
            content=content,
            url=article_url,
            category=category,
            image_url=self.parse_image_url(),
            auther=self.parse_auther(),
            published_at=self.parse_published_at(),
            related_articles=self.parse_related_articles(),
            is_premium=False,
            is_preview=False,
            created_at=datetime.utcnow(),
        )
