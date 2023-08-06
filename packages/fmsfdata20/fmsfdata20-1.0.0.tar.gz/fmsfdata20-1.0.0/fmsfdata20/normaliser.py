import logging
from typing import Literal
from uuid import uuid4

from xsdata.models.enums import DataType

from fmsfdata20.schema import Schema
from fmsfdata20.settings import setup_logger
from fmsfdata20.stream_parser.events import EndNode, StartNode, Value

logger = logging.getLogger(__name__)


def generate_primary_key(generator: Literal["sequence", "uuid"], pk: tuple):
    if generator == "sequence":
        return pk
    if generator == "uuid":
        return uuid4()

    raise Exception(f"It's not possible to detect generator {generator}")


def set_primary_keys(stream, schema: Schema):
    """yield missing primary keys"""
    pk_fields = schema.primary_keys_with_generator_required
    pks = set()
    for event in stream:
        yield event
        if isinstance(event, StartNode) and hasattr(event, "record_id"):
            pk = event.pk
            record_pk_fields = [
                field
                for field in pk_fields
                if field.record.id == event.record_id and pk not in pks
            ]
            for field in record_pk_fields:
                generator = field.extras.get("generator")
                primary_key_value = generate_primary_key(generator, pk)
                yield Value(
                    type=DataType.from_code("str"),
                    record_id=field.record.id,
                    field_id=field.id,
                    value=primary_key_value,
                    pk=pk,
                    context=field.context,
                )
                pks.add(pk)


def detect_foreign_keys(stream, schema: Schema):
    """
    Adds events for foreign keys.
    Assumes they are all missing.
    I think it is yielding repeated values - check that and only yield the necessary ones
    """
    parents = []
    record = None
    for event in stream:
        if isinstance(event, StartNode):
            if new_record := schema.get_record_by_context(event.context):
                record = new_record
                for fk_field in record.foreign_keys:
                    fk_record_id, _ = fk_field.foreign_keys[0].uid.split(".")
                    parent_match = next(
                        iter([p for p in parents if p.record_id == fk_record_id]), None
                    )
                    yield Value(
                        type=DataType.from_code("str"),
                        record_id=record.id,
                        field_id=fk_field.id,
                        value=None,
                        pk=event.pk,
                        parent_record_pk=parent_match.pk,
                        context=fk_field.context,
                    )
                parents.append(event)

        elif isinstance(event, EndNode):
            if (
                record is not None
                and schema.get_record_by_context(event.context) == record
            ):
                record = None

        yield event
