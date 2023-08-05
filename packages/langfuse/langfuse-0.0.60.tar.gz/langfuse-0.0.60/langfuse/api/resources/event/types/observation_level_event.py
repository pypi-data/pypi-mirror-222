# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObservationLevelEvent(str, enum.Enum):
    DEBUG = "DEBUG"
    DEFAULT = "DEFAULT"
    WARNING = "WARNING"
    ERROR = "ERROR"

    def visit(
        self,
        debug: typing.Callable[[], T_Result],
        default: typing.Callable[[], T_Result],
        warning: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObservationLevelEvent.DEBUG:
            return debug()
        if self is ObservationLevelEvent.DEFAULT:
            return default()
        if self is ObservationLevelEvent.WARNING:
            return warning()
        if self is ObservationLevelEvent.ERROR:
            return error()
