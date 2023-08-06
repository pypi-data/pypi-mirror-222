from abc import ABCMeta

from news_toolkit_api.db import Article
from news_toolkit_api.repository.interface import Repository


class ArticleRepository(Repository[Article], metaclass=ABCMeta):
    pass
