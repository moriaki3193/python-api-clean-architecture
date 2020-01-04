"""Entity Typing
"""
from typing import Generic, TypeVar

# ref: https://pypi.org/project/attrs/
from attr import dataclass


T = TypeVar('T')


@dataclass(frozen=True)
class Collection(Generic[T]):
    """Collection of T.
    """
    values: [T]

    def map(self, func) -> map:
        return map(func, self.values)
