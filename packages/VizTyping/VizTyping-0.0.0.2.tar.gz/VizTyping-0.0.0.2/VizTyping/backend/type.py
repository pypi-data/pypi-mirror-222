from enum import Enum


class VizorBackendTypeDoc(Enum):
    """
    后端实例类型
    """
    INFERENCE = "inference"
    TRAINING = "training"
    BSL = "bsl"
