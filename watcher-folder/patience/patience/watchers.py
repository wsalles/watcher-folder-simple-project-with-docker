"""Pattern Watcher Module"""
from .watchdog_handlers import WatcherEventHandler
from .watchdog_observers import WatcherPollingObserver

class PatternWatcher():
    """Pattern Watcher Class"""
    def __init__(self, callback, workdir, ext,
                 timeout=3, recursive=False, blocking=False):
        self._observer = WatcherPollingObserver()
        handler2 = WatcherEventHandler(callback, ext, timeout)
        self._observer.schedule(handler2, workdir, recursive=recursive)
        self._blocking = blocking

    def start(self):
        """Start Watcher"""
        self._observer.start()
        if self._blocking:
            self._observer.join()

    def stop(self):
        """Stop Watcher"""
        self._observer.stop()
