"""
"""
from typing import Protocol

from src.domain.article import Articles


class ArticleRepository(Protocol):
    async def get_list(self, page: int) -> Articles:
        ...
