from abc import ABCMeta, abstractmethod
from datetime import datetime

from bs4 import BeautifulSoup

from news_toolkit_api.client import fetch_content
from news_toolkit_api.db import Article, Feed, RelatedArticle


class ArticleRepository(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.html_text: str | None = None
        self.soup: BeautifulSoup | None = None

    @abstractmethod
    def build_article_url(self, article_id: str) -> str:
        pass

    @abstractmethod
    def build_feed_url(self, category: str) -> str:
        pass

    @abstractmethod
    def parse_title(self, soup: BeautifulSoup) -> str | None:
        pass

    @abstractmethod
    def parse_content(self, soup: BeautifulSoup) -> list[str] | None:
        pass

    @abstractmethod
    def parse_category(self, soup: BeautifulSoup) -> str | None:
        pass

    @abstractmethod
    def parse_image_url(self, soup: BeautifulSoup) -> str | None:
        pass

    @abstractmethod
    def parse_auther(self, soup: BeautifulSoup) -> str | None:
        pass

    @abstractmethod
    def parse_published_at(self, soup: BeautifulSoup) -> datetime | None:
        pass

    @abstractmethod
    def parse_related_articles(self, soup: BeautifulSoup) -> list[RelatedArticle]:
        pass

    @abstractmethod
    def parse_feed(self, soup: BeautifulSoup, category: str) -> list[Feed] | None:
        pass

    async def fetch_content(self, article_id: str) -> Article | None:
        article_url = self.build_article_url(article_id)
        html_text = await fetch_content(article_url)
        if not html_text:
            return None

        soup = BeautifulSoup(html_text, features="html5lib")
        if not soup:
            return None

        title = self.parse_title(soup)
        content = self.parse_content(soup)
        category = self.parse_category(soup)
        if not title or not content or not category:
            return None

        return Article(
            article_id=article_id,
            title=title,
            content=content,
            url=article_url,
            category=category,
            image_url=self.parse_image_url(soup),
            auther=self.parse_auther(soup),
            published_at=self.parse_published_at(soup),
            related_articles=self.parse_related_articles(soup),
            is_premium=False,
            is_preview=False,
            created_at=datetime.utcnow(),
        )

    async def fetch_feed(self, category: str) -> list[Feed] | None:
        feed_url = self.build_feed_url(category)
        html_text = await fetch_content(feed_url)
        if not html_text:
            return None

        soup = BeautifulSoup(html_text, features="html5lib")
        if not soup:
            return None

        return self.parse_feed(soup, category)
