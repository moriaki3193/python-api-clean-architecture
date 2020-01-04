"""Article Entity
"""
from dataclasses import dataclass

from src.domain.collection import Collection


@dataclass(frozen=True)
class Article:
    """Article entity
    """
    id: str
    body: str


@dataclass(frozen=True)
class Articles(Collection[Article]):
    """A collecton of Article entities
    """
    values: [Article]
