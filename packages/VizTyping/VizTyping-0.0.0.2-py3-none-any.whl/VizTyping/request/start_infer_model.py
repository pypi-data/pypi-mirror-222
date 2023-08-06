from typing import List
from VizTyping.backend.info import VizorBackendInfoDoc
from enum import Enum
from docarray import BaseDoc
from typing import Optional


class StartInferModelDoc(BaseDoc):
    versionId: int
    modelPath: str
    modelName: str
    backendName: str
    labelList: List[str]


class InferModelStatus(Enum):
    PREPARING = 0
    RUNNING = 1
    STOPPED = 2


class InferModelInfoDoc(BaseDoc):
    backendInfo:  Optional[VizorBackendInfoDoc] = None
    modelInfo: StartInferModelDoc = None
    modelStatus: Optional[InferModelStatus] = None
