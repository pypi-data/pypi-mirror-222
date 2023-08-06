from itertools import chain
from typing import Any, Dict, Iterable, Iterator, List, Mapping, Union

from ._table_key import DataKey

StringOrStringList = Union[str, Iterable[str]]


def _to_string_list(index_columns: StringOrStringList) -> List[str]:
    if isinstance(index_columns, str):
        return [index_columns]
    else:
        return list(index_columns)


class DataRow(Mapping[str, Any]):
    def __init__(self, pk: DataKey, **kwargs):
        self._data: Dict[str, Any] = {}
        self._pk: DataKey = pk
        for k, v in kwargs.items():
            self[k] = v

    @property
    def pk(self) -> DataKey:
        return self._pk

    def reindex(self, index_columns: StringOrStringList) -> "DataRow":
        index_columns = _to_string_list(index_columns)
        key_cols = {}
        values = {}
        for key in self:
            if key in index_columns:
                key_cols[key] = self[key]
            else:
                values[key] = self[key]
        row = DataRow(DataKey(**key_cols), **values)
        return row

    def prefix_columns(self, prefix: str) -> "DataRow":
        key_cols = {f"{prefix}{k}": v for k, v in self._pk.items()}
        values = {f"{prefix}{k}": v for k, v in self._data.items()}
        row = DataRow(DataKey(**key_cols), **values)
        return row

    def __getitem__(self, key: str) -> Any:
        if key in self._pk:
            return self._pk[key]
        return self._data[key]

    def __getattr__(self, item) -> Any:
        return self[item]

    def __setitem__(self, key: str, value: Any) -> None:
        if key in self._pk:
            raise KeyError(f"Cannot change primary key {key} in DataRow")
        self._data[key] = value

    def __iter__(self) -> Iterator[str]:
        return chain(self._pk.keys(), self._data.keys())

    def __len__(self):
        return len(self._data) + len(self._pk)

    def __eq__(self, other):
        if isinstance(other, Mapping):
            return dict(self) == dict(other)

    def __repr__(self):
        return f"DataRow({dict(self)})"

    def __str__(self):
        return str(dict(self))
