import os

class Path:
    _zns_util_box = os.path.dirname(os.path.abspath(__file__))
    RESOURCE = os.path.join(_zns_util_box, "_resource")