from uuid import uuid4

from xsdata.models.enums import DataType

from fmsfdata.schema import Schema
from fmsfdata.stream_parser.events import EndNode, StartNode, Value


def identify_fields(stream, schema: Schema):
    """
    set field type and field name.
    It's important to note that one record can start within another record.
    """
    record = None
    count = 0
    for event in stream:
        if isinstance(event, StartNode):
            if new_record := schema.get_record_by_context(event.context):
                record = new_record
                event = event.from_event(
                    event, record_id=record.id, pk=record.context + (count,)
                )
        elif isinstance(event, EndNode):
            if (
                record is not None
                and schema.get_record_by_context(event.context) == record
            ):
                event = event.from_event(
                    event, record_id=record.id, pk=record.context + (count,)
                )
                record = None
                count += 1
        yield event

        if isinstance(event, StartNode) and record is not None:
            if field := record.get_field_by_context(event.context):
                value_event = next(stream)
                if isinstance(value_event, Value):
                    if isinstance(field.datatype, str):
                        field_type = DataType.from_code(field.datatype.lower())
                    elif field.datatype.uid in schema.datatypes:
                        field_type = field.datatype
                    else:
                        # TODO - should we use string as a default?
                        field_type = DataType.from_code("string")

                    value_event = value_event.from_event(
                        value_event,
                        type=field_type,
                        record_id=record.id,
                        field_id=field.id,
                        pk=record.context + (count,),
                    )
                yield value_event
