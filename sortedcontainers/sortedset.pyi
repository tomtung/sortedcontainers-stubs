import typing
from typing import (
    Any,
    AbstractSet,
    Callable,
    Generic,
    Hashable,
    Iterable,
    Iterator,
    List,
    MutableSet,
    Optional,
    Sequence,
    Tuple,
    Type,
    Set,
    TypeVar,
    Union,
)

# --- Global

_T = TypeVar("_T", bound=Hashable)
_S = TypeVar("_S", bound=Hashable)
_SS = TypeVar("_SS", bound="SortedSet")
_Key = Callable[[_T], Any]

class SortedSet(MutableSet[_T], Sequence[_T]):
    def __init__(self, iterable: Optional[Iterable[_T]] = ..., key: Optional[_Key] = ...) -> None: ...
    @classmethod
    def _fromset(cls, values: Set[_T], key: Optional[_Key] = ...) -> SortedSet[_T]: ...
    @property
    def key(self) -> Optional[_Key]: ...
    def __contains__(self, value: Any) -> bool: ...
    @typing.overload
    def __getitem__(self, index: int) -> _T: ...
    @typing.overload
    def __getitem__(self, index: slice) -> List[_T]: ...
    def __delitem__(self, index: Union[int, slice]) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __lt__(self, other: Iterable[_T]) -> bool: ...
    def __gt__(self, other: Iterable[_T]) -> bool: ...
    def __le__(self, other: Iterable[_T]) -> bool: ...
    def __ge__(self, other: Iterable[_T]) -> bool: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __reversed__(self) -> Iterator[_T]: ...
    def add(self, value: _T) -> None: ...
    _add = add
    def clear(self) -> None: ...
    def copy(self: _SS) -> _SS: ...
    def __copy__(self: _SS) -> _SS: ...
    def count(self, value: _T) -> int: ...
    def discard(self, value: _T) -> None: ...
    _discard = discard
    def pop(self, index: int = ...) -> _T: ...
    def remove(self, value: _T) -> None: ...
    def difference(self, *iterables: Iterable[_S]) -> SortedSet[Union[_T, _S]]: ...
    __sub__ = difference
    def difference_update(self, *iterables: Iterable[_S]) -> SortedSet[Union[_T, _S]]: ...
    __isub__ = difference_update
    def intersection(self, *iterables: Iterable[_S]) -> SortedSet[Union[_T, _S]]: ...
    __and__ = intersection
    __rand__ = __and__
    def intersection_update(self, *iterables: Iterable[_S]) -> SortedSet[Union[_T, _S]]: ...
    __iand__ = intersection_update
    def symmetric_difference(self, other: Iterable[_S]) -> SortedSet[Union[_T, _S]]: ...
    __xor__ = symmetric_difference
    __rxor__ = __xor__
    def symmetric_difference_update(self, other: Iterable[_S]) -> SortedSet[Union[_T, _S]]: ...
    __ixor__ = symmetric_difference_update
    def union(self, *iterables: Iterable[_S]) -> SortedSet[Union[_T, _S]]: ...
    __or__ = union
    __ror__ = __or__
    def update(self, *iterables: Iterable[_S]) -> SortedSet[Union[_T, _S]]: ...
    __ior__ = update
    _update = update
    def __reduce__(self) -> Tuple[Type[SortedSet[_T]], Set[_T], Callable[[_T], Any]]: ...
    def __repr__(self) -> str: ...
    def _check(self) -> None: ...
