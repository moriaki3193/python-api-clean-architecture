"""So-called API controller
"""
import asyncio

from flask import jsonify, request

from src.domain.article import Articles
from src.interface.usecase.article import ArticleUsecase


class ArticleResource:
    article_usecase: ArticleUsecase

    def __init__(self, article_usecase: ArticleUsecase) -> None:
        self.article_usecase = article_usecase

    def index(self, page):
        main_group: Articles = asyncio.run(self.article_usecase.get_list(page))
        return jsonify(articles_response(main_group))


def articles_response(articles: Articles) -> dict:
    return {
        'items': [{
            'id': article.id,
            'body': article.body,
        } for article in articles.values]
    }
