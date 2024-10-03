from collections import OrderedDict
from collections.abc import MutableMapping
from typing import Generic, ItemsView, Iterator, TypeVar, ValuesView

T = TypeVar('T')

class LRUCache(MutableMapping[str, T], Generic[T]):
    """A more Pythonic and efficient implementation of LRU Cache using `OrderedDict`."""
    
    def __init__(self, max_length: int) -> None:
        """Initialize the LRUCache with a specific max_length."""
        self._cache: OrderedDict[str, T] = OrderedDict()
        self._max_length = max_length

    def __getitem__(self, key: str) -> T:
        """Retrieve an item from the cache and move it to the end if found."""
        if key not in self._cache:
            raise KeyError(f"Key {key} not found in the cache")
        val = self._cache[key]
        self._cache.move_to_end(key)  # Move accessed item to the end (most recently used)
        return val

    def __setitem__(self, key: str, value: T) -> None:
        """Insert or update an item in the cache. Evict the least recently used item if necessary."""
        if key in self._cache:
            self._cache.move_to_end(key)
        self._cache[key] = value
        if len(self._cache) > self._max_length:
            self._cache.popitem(last=False)  # Remove the oldest item (least recently used)

    def __delitem__(self, key: str) -> None:
        """Delete an item from the cache."""
        del self._cache[key]

    def __iter__(self) -> Iterator[str]:
        """Iterate over the cache keys."""
        return iter(self._cache)

    def __len__(self) -> int:
        """Return the number of items in the cache."""
        return len(self._cache)

    def get(self, key: str, default: T = None) -> T | None:
        """Safely get an item from the cache without raising KeyError."""
        try:
            return self[key]
        except KeyError:
            return default

    def values(self) -> ValuesView[T]:
        """Return an iterator over the values in the cache."""
        return self._cache.values()

    def items(self) -> ItemsView[str, T]:
        """Return an iterator over the (key, value) pairs in the cache."""
        return self._cache.items()

    def __repr__(self) -> str:
        """Return a string representation of the cache."""
        return f"LRUCache(max_length={self._max_length}, items={list(self._cache.items())})"
