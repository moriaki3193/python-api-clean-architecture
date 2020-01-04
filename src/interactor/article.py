"""
"""
from src.domain.article import Articles
from src.interface.repository.article import ArticleRepository


class ArticleInteractor:
    """
    """
    article_repository: ArticleRepository

    def __init__(self, article_repository: ArticleRepository) -> None:
        self.article_repository = article_repository

    async def get_list(self, page: int) -> Articles:
        return await self.article_repository.get_list(page)
