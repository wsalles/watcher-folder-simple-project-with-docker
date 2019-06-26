import os

data = {
    'WATCHDIR': os.environ['WATCHDIR'],
    'WATCH_FOLDER': os.environ['WATCH_FOLDER'],
    'DESTINATION': os.environ['DESTINATION'],
    'TIMEOUT': int(os.environ['TIMEOUT']),
    'EXT': ['*.mxf', '*.MXF'],
    'REMOVE_META': False
}
