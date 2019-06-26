"""Watchdog events module"""
from watchdog.events import FileSystemEvent

# pylint: disable=too-few-public-methods
class GarbageCollectorEvent(FileSystemEvent):
    """Watchdog Garbage Collector Event"""
    event_type = 'gc'

    def __init__(self, datetime_event):
        super(GarbageCollectorEvent, self).__init__('')
        self._datetime_event = datetime_event

    @property
    def datetime(self):
        """retun datetime"""
        return self._datetime_event

    def __repr__(self):
        return "<%(class_name)s: datetime=%(datetime)r>" %\
               dict(class_name=self.__class__.__name__,
                    datetime=self._datetime_event)
