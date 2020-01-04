"""Article Entity
"""
from dataclasses import dataclass
from typing import Collection

from .collection import _Collection


@dataclass(frozen=True)
class Article:
    """Article entity
    """
    id: str
    body: str


@dataclass(frozen=True)
class Articles(_Collection[Article]):
    """A collecton of Article entities
    """
    values: Collection[Article]
