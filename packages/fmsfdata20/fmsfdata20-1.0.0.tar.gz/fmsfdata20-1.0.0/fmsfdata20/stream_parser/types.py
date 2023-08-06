from typing import Callable, Iterator, Union

from fmsfdata20.stream_parser import events

FilteredValue = Union[events.ParseEvent, Iterator[events.ParseEvent]]
EventFilter = Callable[[events.ParseEvent], FilteredValue]
FilterErrorHandler = Callable[[events.ParseEvent, Exception], FilteredValue]
