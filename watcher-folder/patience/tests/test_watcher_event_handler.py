import pytest
from datetime import timedelta
from patience.watchdog_handlers import WatcherEventHandler
from patience.watchdog_events import GarbageCollectorEvent
from watchdog.events import FileCreatedEvent, FileModifiedEvent

def test_watcher_event_handler():
    def callback():
        pass
    handler = WatcherEventHandler(callback, ['*.txt'])
    handler.dispatch(FileModifiedEvent('file.txt'))
    assert not handler.files

    handler.dispatch(FileCreatedEvent('file.rst'))
    assert 'file.rst' not in handler.files

    handler.dispatch(FileCreatedEvent('file.txt'))
    assert 'file.txt' in handler.files

    old_dt = handler.files['file.txt']
    handler.dispatch(FileModifiedEvent('file.txt'))
    assert old_dt < handler.files['file.txt']

    old_dt += timedelta(seconds=4)
    handler.dispatch(GarbageCollectorEvent(old_dt))
    assert not handler.files
    