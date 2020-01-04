"""Entity Typing
"""
from typing import Callable, Collection, Generic, Iterator, TypeVar

# ref: https://pypi.org/project/attrs/
from attr import dataclass


S = TypeVar('S')
T = TypeVar('T')


@dataclass(frozen=True)
class _Collection(Generic[T]):
    """Collection of T.
    """
    values: Collection[T]

    def map(self, func: Callable[[T], S]) -> Iterator[S]:
        return map(func, self.values)
