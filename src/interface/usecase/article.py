"""Use Cases <-> Entities
"""
from typing import Protocol

from src.domain.article import Articles


class ArticleUsecase(Protocol):
    async def get_list(self, page: int) -> Articles:
        ...
