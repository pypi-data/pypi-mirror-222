from typing import Callable, Iterator, Union

from fmsfdata.stream_parser import events

FilteredValue = Union[events.ParseEvent, Iterator[events.ParseEvent]]
EventFilter = Callable[[events.ParseEvent], FilteredValue]
FilterErrorHandler = Callable[[events.ParseEvent, Exception], FilteredValue]
