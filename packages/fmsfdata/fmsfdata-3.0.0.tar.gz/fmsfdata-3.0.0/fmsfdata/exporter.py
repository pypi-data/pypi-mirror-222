from typing import Generator

import tablib
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod, XmlTime
from xsdata.models.enums import DataType

from fmsfdata.datastore import DataKey, DataStore
from fmsfdata.schema import Schema
from fmsfdata.stream_parser import events
from fmsfdata.stream_parser.filters.context import generator_with_value


def export_value(event_type, value):
    """
    export value to standard python format
    (opinionated maybe, might not be the best approach)
    """
    if isinstance(value, XmlTime):
        return value.to_time()
    if isinstance(value, XmlDate):
        return value.to_date()
    if isinstance(value, XmlDateTime):
        return value.to_datetime()
    if isinstance(value, XmlPeriod):
        if event_type == DataType.G_YEAR:
            return value.year
        if event_type == DataType.G_MONTH:
            return value.month
        if event_type == DataType.G_DAY:
            return value.day
        # for month-day and year-month export as string
        return str(value)
    return value


@generator_with_value
def populate_datastore(
    stream, schema: Schema
) -> Generator[events.ParseEvent, None, DataStore]:
    datastore = DataStore()
    primary_keys_found = {}

    for event in stream:
        value = event.get("value")
        context = event.get("context")
        pk = event.get("pk")
        parent_record_pk = event.get("parent_record_pk")
        event_type = event.get("type")
        if field := schema.get_field_by_context(context):
            if field.primary_key and not field.foreign_keys and pk:
                # field is a primary key - save it for possibly setting it as a foreign key
                primary_keys_found[pk] = value

            if parent_record_pk and not value:
                # field is a missing foreign key - get the corresponding value
                value = primary_keys_found.get(parent_record_pk, None)

        if value is not None and pk:
            key = DataKey(pk=pk)
            datastore.put_value(
                record_id=event.record_id,
                key=key,
                field_id=event.field_id,
                value=export_value(event_type, value),
            )
        yield event
    return datastore


def datastore_to_databook(datastore: DataStore, schema: Schema) -> tablib.Databook:
    book = tablib.Databook()
    for record in schema.records.values():
        headers = [f.id for f in record.fields]
        sheet = tablib.Dataset(title=record.id, headers=headers)
        book.add_sheet(sheet)

        table = datastore.get_table(record.id)
        if table:
            for pk in table:
                values = [table.get_value(pk, field_id=f.id) for f in record.fields]
                sheet.append(values)
    return book
