from docarray import BaseDoc
from VizTyping.backend.info import VizorBackendInfoDoc
from typing import List, Optional


class ParametersDoc(BaseDoc):
    imgScale: str
    epoch: int
    batchSize: int
    learningRate: float


class AddTrainTaskDoc(BaseDoc):
    versionId: int
    baseVersionId: int
    baseVersionTrainFile: str = ""
    backendName: str = ""
    modelName: str = ""
    dataPath: List[str]
    labelList: List[str]
    dataType: str = ""
    dataSetRatio: List[float]
    parameters: ParametersDoc = None


class TrainTaskInfoDoc(BaseDoc):
    backendInfo: Optional[VizorBackendInfoDoc] = None
    taskInfo: AddTrainTaskDoc = None


