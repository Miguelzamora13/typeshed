from _typeshed import AnyPath
from types import CodeType
from typing import Any, Callable, Dict, Optional, Tuple, TypeVar, Union

def run(statement: str, filename: Optional[str] = ..., sort: Union[str, int] = ...) -> None: ...
def runctx(
    statement: str, globals: Dict[str, Any], locals: Dict[str, Any], filename: Optional[str] = ..., sort: Union[str, int] = ...
) -> None: ...

_SelfT = TypeVar("_SelfT", bound=Profile)
_T = TypeVar("_T")
_Label = Tuple[str, int, str]

class Profile:
    stats: dict[_Label, tuple[int, int, int, int, dict[_Label, tuple[int, int, int, int]]]]  # undocumented
    def __init__(
        self, timer: Callable[[], float] = ..., timeunit: float = ..., subcalls: bool = ..., builtins: bool = ...
    ) -> None: ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...
    def print_stats(self, sort: Union[str, int] = ...) -> None: ...
    def dump_stats(self, file: AnyPath) -> None: ...
    def create_stats(self) -> None: ...
    def snapshot_stats(self) -> None: ...
    def run(self: _SelfT, cmd: str) -> _SelfT: ...
    def runctx(self: _SelfT, cmd: str, globals: Dict[str, Any], locals: Dict[str, Any]) -> _SelfT: ...
    def runcall(self, __func: Callable[..., _T], *args: Any, **kw: Any) -> _T: ...

def label(code: Union[str, CodeType]) -> _Label: ...  # undocumented
