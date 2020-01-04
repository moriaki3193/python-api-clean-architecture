"""
"""
from typing import Protocol


class ArticleDriver(Protocol):
    async def get_articles(self, page: int) -> dict:
        ...
