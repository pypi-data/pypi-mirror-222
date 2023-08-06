from enum import Enum


class VizorBackendStatusDoc(Enum):
    """
    后端状态
    """
    REGISTERED = 0
    REGISTERED_FAILED = 1
    RUNNING = 2
    UNREGISTERED = 3
    DISCONNECTED = 4