import logging
from typing import Literal

from sfdata.converter import convert_types
from sfdata.datastore import DataStore
from sfdata.exporter import datastore_to_databook, populate_datastore
from sfdata.identifier import identify_fields
from sfdata.normaliser import detect_foreign_keys, set_primary_keys
from sfdata.schema import Schema
from sfdata.settings import setup_logger
from sfdata.stream_parser.filters.context import add_context
from sfdata.stream_parser.parser.xml import dom_parse

setup_logger()
logger = logging.getLogger(__name__)


def debug(stream):
    """only used to consume the stream"""
    for _ in stream:
        pass


def standardise(schema: Schema, file, output: Literal["dataframes", "databook"]):
    logger.info(f"starting standardisation for file {file} and schema {schema}")
    stream = dom_parse(file)
    stream = add_context(stream)
    stream = identify_fields(stream, schema)
    stream = convert_types(stream)
    stream = set_primary_keys(stream=stream, schema=schema)
    stream = detect_foreign_keys(stream=stream, schema=schema)

    datastore, stream = populate_datastore(stream=stream, schema=schema)
    stream = debug(stream)
    datastore: DataStore = datastore.value
    book = datastore_to_databook(datastore, schema)

    logger.info(f"finished standardisation for file {file} and schema {schema}")
    if output == "dataframes":
        return {sheet.title: sheet.export("df") for sheet in book.sheets()}
    elif output == "databook":
        return book
    return []
