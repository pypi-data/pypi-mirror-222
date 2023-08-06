import warnings
from collections import namedtuple
from functools import cached_property, lru_cache
from typing import Any, Iterable, List, Mapping, Optional, Union

import humps
from xsdata.exceptions import ConverterWarning
from xsdata.formats.converter import converter
from xsdata.models.enums import DataType as xsDataType

from ._proxy import Proxy
from ._types import standard_types


class SchemaItem:
    def __init__(self, id, schema, /, extras: Mapping[str, Any] = None):
        self._id = id
        self._schema = schema
        self._extras = extras or {}

    @property
    def id(self) -> str:
        return self._id

    @property
    def uid(self) -> str:
        return self.id

    @property
    def schema(self) -> "Schema":
        return self._schema

    @property
    def extras(self) -> Mapping[str, Any]:
        return self._extras

    def __repr__(self):
        return f"{self.__class__.__name__}(uid={self.uid!r})"


class Datatype(SchemaItem):
    def __init__(
        self,
        id,
        /,
        schema: "Schema" = None,
        extras: Mapping[str, Any] = None,
    ):
        if schema is None:
            schema = Proxy()
        super().__init__(id, schema, extras=extras)

    @staticmethod
    def from_value(value):
        if isinstance(value, Datatype):
            return value
        elif isinstance(value, str):
            return Datatype(value)
        elif isinstance(value, dict):
            value = value.copy()
            id = value.pop("id")
            return Datatype(id, extras=value)

    def deserialize(self, value):
        base = self.extras.get("base", None) or self.uid
        enumeration = self.extras.get("enumeration", None)
        if not base and not enumeration:
            # TODO - accept other custom datatypes?
            raise Exception(
                f"Currently you must define your base and enumeration for the custom Datatype to work! {self}"
            )

        datatype = xsDataType.from_code(base)

        def _raise_warning():
            warnings.warn(
                f"Failed to convert value `{value}` to one of {enumeration}",
                ConverterWarning,
            )

        if isinstance(enumeration, dict):
            if all(isinstance(key, int) for key in enumeration.keys()):
                # keys are integers
                try:
                    value_as_key = int(value)
                except ValueError:
                    # key is not an integer - check if in values
                    if value not in enumeration.values():
                        _raise_warning()
                else:
                    if value_as_key not in enumeration.keys():
                        _raise_warning()
                    else:
                        # get value given the enum key
                        value = enumeration[value_as_key]
            else:
                try:
                    value = enumeration[value]
                except KeyError:
                    _raise_warning()

            value = converter.deserialize(value, [datatype.type])
        elif isinstance(enumeration, Iterable):
            if value not in enumeration:
                _raise_warning()
            value = converter.deserialize(value, [datatype.type])
        return value


class CategoricalValue(SchemaItem):
    id: str


class Categories(SchemaItem, Mapping[str, CategoricalValue]):
    id: str


class Field(SchemaItem):
    def __init__(
        self,
        id,
        /,
        record: "Record" = None,
        primary_key: bool = False,
        foreign_keys: List[Union[str, "Field"]] = None,
        type: Union[str, Datatype] = None,
        extras: Mapping[str, Any] = None,
    ):
        if record is None:
            record = Proxy()
        super().__init__(id, record.schema, extras=extras)

        if type is None:
            type = "string"
        if isinstance(type, Datatype):
            type = type.id

        self._record = record
        self._type = type
        self._primary_key = primary_key
        self._foreign_keys = foreign_keys

    @property
    def uid(self):
        return f"{self.record.uid}.{self.id}"

    @property
    def record(self) -> "Record":
        return self._record

    @property
    def datatype(self) -> Datatype:
        return self._schema.datatypes.get(self._type, self._type)

    @property
    def primary_key(self) -> bool:
        return self._primary_key

    @property
    def foreign_keys(self) -> List["Field"]:
        return [
            fk if isinstance(fk, Field) else self._schema.fields[fk]
            for fk in self._foreign_keys or []
        ]

    @cached_property
    def context(self) -> Iterable[str]:
        if path := self.extras.get("path", ""):
            if path == ".":
                return self.record.context
            return tuple(path.split("/"))
        return self.record.context + (self.id,)

    @staticmethod
    def from_value(value):
        if isinstance(value, Field):
            return value
        elif isinstance(value, str):
            if value.startswith("*"):
                return Field(value[1:], primary_key=True)
            else:
                return Field(value)
        elif isinstance(value, dict):
            value = value.copy()
            id = value.pop("id")
            primary_key = value.pop("primary_key", False)
            foreign_keys = value.pop("foreign_keys", None)
            type = value.pop("type", None)
            return Field(
                id,
                type=type,
                primary_key=primary_key,
                foreign_keys=foreign_keys,
                extras=value,
            )
        raise ValueError(f"Cannot convert {value!r} to Field")


class Record(SchemaItem, Mapping[str, Field]):
    def __init__(
        self,
        id: str,
        fields: List["Field"],
        /,
        schema: "Schema" = None,
        extras: Mapping[str, Any] = None,
    ):
        if schema is None:
            schema = Proxy()
        super().__init__(id, schema, extras=extras)
        fields = [Field.from_value(field) for field in fields]
        Proxy.init_proxy([f.record for f in fields], self)
        self._fields = {f.id: f for f in fields}

    @property
    def fields(self) -> List[Field]:
        return [f for f in self.values() or []]

    @cached_property
    def context(self) -> Iterable[str]:
        if path := self.extras.get("path", ""):
            return tuple(path.split("/"))
        return (self.id,)

    @property
    def primary_keys(self) -> List[Field]:
        return [f for f in self.values() or [] if f.primary_key]

    @property
    def foreign_keys(self) -> List[Field]:
        return [f for f in self.values() or [] if f.foreign_keys]

    @property
    def key_class(self) -> namedtuple:
        return namedtuple(
            humps.pascalize(f"{self.id}_key"),
            ["record"] + [k.id for k in self.primary_keys],
        )

    @property
    def record_class(self) -> namedtuple:
        cls = namedtuple(
            humps.pascalize(f"{self.id}_record"), [f.id for f in self.values()]
        )
        cls._record = self

        class MyRecord(cls):
            @property
            def field_values(self):
                return self._asdict()

            @property
            def record(self):
                return self._record

            @property
            def primary_key(self):
                return self._record.key_class(
                    **{pk.id: getattr(self, pk.id) for pk in self._record.primary_keys}
                )

        MyRecord.__name__ = cls.__name__
        MyRecord.__qualname__ = cls.__qualname__
        return MyRecord

    def __getitem__(self, key):
        return self._fields[key]

    def __iter__(self):
        return iter(self._fields)

    def __len__(self):
        return len(self._fields)

    @staticmethod
    def from_value(value):
        if isinstance(value, Record):
            return value
        elif isinstance(value, dict):
            value = value.copy()
            id = value.pop("id")
            fields = value.pop("fields")
            if isinstance(fields, dict):
                fields = [
                    Field.from_value({"id": f_id, **f}) for f_id, f in fields.items()
                ]
            return Record(id, fields, extras=value)

    def get_key(self, **kwargs):
        return self.key_class(record=self.id, **kwargs)

    def get_field_by_context(self, context: Iterable[str]) -> Optional[Field]:
        for field in self.fields:
            if context == field.context:
                return field
        return None


class _SchemaMapping(Mapping[str, SchemaItem]):
    def __init__(self, values: List[Any]):
        self._values = {v.id: v for v in values}

    def __getitem__(self, key):
        return self._values[key]

    def __iter__(self):
        return iter(self._values.keys())

    def __len__(self):
        return len(self._values)


class _SchemaFieldMapping(Mapping[str, Field]):
    def __init__(self, schema: "Schema"):
        self._schema = schema

    def __getitem__(self, key):
        record_id, field_id = key.split(".", 1)
        return self._schema.records[record_id][field_id]

    def __iter__(self):
        for record in self._schema.records.values():
            for field in record.values():
                yield f"{record.id}.{field.id}"

    def __len__(self):
        return len(list(self.__iter__()))


class Schema:
    def __init__(self, records, id=None, version=None, datatypes=None, extras=None):
        if datatypes is None:
            datatypes = standard_types
        datatypes = [Datatype.from_value(d) for d in datatypes]
        Proxy.init_proxy([dt.schema for dt in datatypes], self)
        Proxy.init_proxy([r.schema for r in records], self)
        self._records = _SchemaMapping(records)
        self._datatypes = _SchemaMapping(datatypes)
        self._fields = _SchemaFieldMapping(self)
        self._id = id
        self._version = version
        self._extras = extras or {}

        # Ensure types
        for f in self._fields.values():
            assert f.datatype

    @property
    def records(self) -> Mapping[str, Record]:
        return self._records

    @property
    def datatypes(self) -> Mapping[str, Datatype]:
        return self._datatypes

    @property
    def id(self) -> str:
        return self._id

    @property
    def version(self) -> str:
        return self._version

    @property
    def fields(self) -> Mapping[str, Field]:
        return self._fields

    @property
    def extras(self) -> Mapping[str, Any]:
        return self._extras

    @staticmethod
    def from_value(value):
        if isinstance(value, Schema):
            return value
        elif isinstance(value, dict):
            value = value.copy()
            records = value.pop("records", [])
            datatypes = value.pop("datatypes", None)

            id = value.pop("id")
            version = value.pop("version")

            if isinstance(records, Mapping):
                records = [
                    Record.from_value({"id": r_id, **r}) for r_id, r in records.items()
                ]

            if isinstance(datatypes, Mapping):
                datatypes = [
                    Datatype.from_value({"id": dt_id, **dt})
                    for dt_id, dt in datatypes.items()
                ]

            return Schema(
                id=id,
                version=version,
                records=records,
                datatypes=datatypes,
                extras=value,
            )

    @lru_cache(maxsize=25)
    def get_record_keys(self, record_id):
        try:
            record = self.records[record_id]
        except IndexError:
            return None, tuple()

        return record, tuple(
            (
                pk.id,
                record.id if not pk.foreign_keys else pk.foreign_keys[0].record.id,
            )
            for pk in record.primary_keys
        )

    @cached_property
    def primary_keys(self) -> List[Field]:
        return [f for r in self.records.values() for f in r.primary_keys]

    @cached_property
    def foreign_keys(self) -> List[Field]:
        return [f for r in self.records.values() for f in r.foreign_keys]

    @cached_property
    def primary_keys_with_generator_required(self) -> List[Field]:
        return [
            f
            for r in self.records.values()
            for f in r.primary_keys
            if f.extras.get("generator", None) is not None
        ]

    def get_record_by_context(self, context: Iterable[str]) -> Optional[Record]:
        for record in self.records.values():
            if context == record.context:
                return record
        return None

    def get_field_by_context(self, context: Iterable[str]) -> Optional[Field]:
        for record in self.records.values():
            for field in record.fields:
                if context == field.context:
                    return field
        return None
