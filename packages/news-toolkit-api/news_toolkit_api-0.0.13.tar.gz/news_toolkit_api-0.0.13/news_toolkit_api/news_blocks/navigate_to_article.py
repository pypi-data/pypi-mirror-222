from dataclasses import dataclass


@dataclass(frozen=True)
class NavigateToArticleAction:
    article_id: str
    __identifier = "__navigate_to_article__"

    def type(self) -> str:
        return self.__identifier
