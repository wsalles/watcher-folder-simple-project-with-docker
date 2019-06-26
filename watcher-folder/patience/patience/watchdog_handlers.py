"""Watchdog Handlers Module"""
import logging
from datetime import datetime
from pathtools.patterns import match_any_paths

# pylint: disable=too-few-public-methods
# pylint: disable=broad-except
class WatcherEventHandler:
    """Watcher Event Handler Class"""
    def __init__(self, callback, patterns, timeout=3):
        self.logger = logging.getLogger(__name__)
        self.callback = callback
        self.timeout = timeout
        self.files = {}
        self.patterns = patterns
        self.handlers = {
            'gc': self._gc_handler,
            'created': self._create_handler,
            'modified': self._update_handler,
        }

    def dispatch(self, event):
        """Method called by watchdog when one event is dispatched"""
        self.handlers.get(event.event_type, lambda event: None)(event)

    def _gc_handler(self, event):
        for file in list(self.files.keys()):
            delta = event.datetime - self.files[file]
            if delta.total_seconds() > self.timeout:
                try:
                    self.callback(file)
                except Exception as ex:
                    self.logger.error("Error %s", ex)
                self.logger.info('GC: %s', self.files[file])
                del self.files[file]

    def _create_handler(self, event):
        if match_any_paths([event.src_path], included_patterns=self.patterns):
            self.files[event.src_path] = datetime.now()
            self.logger.info('File created: %s', event)

    def _update_handler(self, event):
        if event.src_path in self.files and match_any_paths([event.src_path],
                                                            included_patterns=self.patterns):
            self.files[event.src_path] = datetime.now()
            self.logger.info('File modified: %s', event)
