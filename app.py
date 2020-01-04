"""
"""
from flask import Flask

from src.driver.article import ArticleDriverImpl
from src.interactor.article import ArticleInteractor
from src.repository.article import ArticleRepositoryImpl
from src.rest.article import ArticleResource
from src.setting import DevConfig


article_resource = ArticleResource(
    article_usecase=ArticleInteractor(
        article_repository=ArticleRepositoryImpl(
            article_driver=ArticleDriverImpl()
        ),
    ),
)

def create_app(config=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    # Routing
    app.add_url_rule('/<page>', view_func=article_resource.index)
    return app
