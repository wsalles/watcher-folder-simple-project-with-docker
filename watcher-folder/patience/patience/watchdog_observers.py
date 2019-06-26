"""Watchdog Observer Module"""
from datetime import datetime
from watchdog.observers.polling import PollingEmitter
from watchdog.observers.api import BaseObserver
from .watchdog_events import GarbageCollectorEvent

class WatcherPollingEmitter(PollingEmitter):
    """Watcher Polling Emitter"""
    def queue_events(self, timeout):
        super().queue_events(timeout)
        with self._lock:
            self.queue_event(GarbageCollectorEvent(datetime.now()))

class WatcherPollingObserver(BaseObserver):
    """Watcher Polling Observer"""
    def __init__(self, timeout=1):
        BaseObserver.__init__(self, emitter_class=WatcherPollingEmitter, timeout=timeout)
