from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar

from bs4 import BeautifulSoup

from news_toolkit_api.client import fetch_content

Content = TypeVar("Content")


class Repository(Generic[Content], metaclass=ABCMeta):
    @abstractmethod
    def build_url(self, id: str) -> str:
        pass

    @abstractmethod
    def parse(self, soup: BeautifulSoup, id: str) -> Content | None:
        pass

    async def fetch_content(self, id: str) -> Content | None:
        html_text = await fetch_content(self.build_url(id))
        if not html_text:
            return None

        soup = BeautifulSoup(html_text, features="html5lib")
        if not soup:
            return None

        return self.parse(soup, id)
