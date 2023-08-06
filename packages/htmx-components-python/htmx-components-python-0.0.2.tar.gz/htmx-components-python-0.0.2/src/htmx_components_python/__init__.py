from __future__ import annotations

import typing as t
from abc import abstractstaticmethod
from dataclasses import dataclass, field
from enum import Enum


@dataclass
class TreeConfig:
    data: t.Callable | list
    lazy: bool = False
    prefix: str = ""
    key_attr: str = "id"
    text_attr: str = "name"
    parent_id_attr: str = "parent_id"
    render_node: t.Callable[[t.Mapping], str] = lambda item: item["name"]
    htmx_endpoint: str = ""
    search: bool = True
    toggle_all: bool = True
    expand_icon: str = "bi-caret-right-fill text-secondary"
    collapse_icon: str = "bi-caret-down-fill text-secondary"

    def __post_init__(self):
        if self.prefix and not self.prefix.endswith("-"):
            self.prefix = f"{self.prefix}-"


@dataclass
class Column:
    attr: str
    text: str = ""
    render: t.Callable = str

    def __post_init__(self):
        if not self.text:
            self.text = self.attr


@dataclass
class GridConfig:
    prefix: str = ""
    columns: t.Iterable[Column | str] = field(default_factory=list)
    table_cls = ""

    def __post_init__(self):
        if self.prefix:
            self.prefix = f"{self.prefix}-"

        self.columns = list(
            map(lambda col: Column(col) if isinstance(col, str) else col, self.columns)
        )

    @abstractstaticmethod
    def get_records(
        page: int = 1,
        page_size: int = 20,
        sorts=list[tuple[str, str]],
        q: str = "",
    ) -> tuple[t.Iterable[t.Any], int]:
        ...


class SelectionMode(Enum):
    NONE = 0
    SINGLE = 1
    MULTI = 2
