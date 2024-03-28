

from dataclasses import dataclass
from typing import Any, Union

@dataclass(frozen=True)
class FrozenNode:
    value: Any
    next: Union[None, 'FrozenNode']

@dataclass(frozen=False)
class MutableNode:
    value: Any
    next: Union[None, 'MutableNode']