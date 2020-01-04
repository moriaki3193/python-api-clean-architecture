"""
"""
from flask import Flask

from src.driver.article import ArticleDriverImpl
from src.interactor.article import ArticleInteractor
from src.repository.article import ArticleRepositoryImpl
from src.rest.article import ArticleResource


app = Flask(__name__)

article_resource = ArticleResource(
    article_usecase=ArticleInteractor(
        article_repository=ArticleRepositoryImpl(
            article_driver=ArticleDriverImpl()
        ),
    ),
)

app.add_url_rule('/', view_func=article_resource.index)
