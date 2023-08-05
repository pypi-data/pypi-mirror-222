# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .observation_level_span import ObservationLevelSpan


class Span(pydantic.BaseModel):
    id: str
    trace_id: str = pydantic.Field(alias="traceId")
    type: str
    name: typing.Optional[str]
    start_time: dt.datetime = pydantic.Field(alias="startTime")
    end_time: typing.Optional[dt.datetime] = pydantic.Field(alias="endTime")
    metadata: typing.Optional[typing.Any]
    input: typing.Optional[typing.Any]
    output: typing.Optional[typing.Any]
    level: ObservationLevelSpan
    status_message: typing.Optional[str] = pydantic.Field(alias="statusMessage")
    parent_observation_id: typing.Optional[str] = pydantic.Field(alias="parentObservationId")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
