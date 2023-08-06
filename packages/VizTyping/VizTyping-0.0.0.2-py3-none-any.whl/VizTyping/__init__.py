from VizTyping.request.rm_infer_task import RmInferTaskDoc
from VizTyping.request.rm_train_task import RmTrainTaskDoc
from VizTyping.request.add_train_task import AddTrainTaskDoc, TrainTaskInfoDoc, ParametersDoc
from VizTyping.request.add_infer_task import AddInferTaskDoc, InferTaskInfoDoc, RouteNodeInferTaskDoc, \
    V2NAddInferTaskDoc, InferTaskRouteDoc
from VizTyping.request.stop_infer_model import StopInferModelDoc
from VizTyping.request.start_infer_model import StartInferModelDoc, InferModelInfoDoc, InferModelStatus
from VizTyping.request.backend_register import RegisterDoc
from VizTyping.backend.type import VizorBackendTypeDoc
from VizTyping.backend.status import VizorBackendStatusDoc
from VizTyping.backend.info import VizorBackendInfoDoc
from VizTyping.meta.frame_meta import VizorFrameMetaDoc
from VizTyping.meta.classifier_meta import VizorClassifierMetaDoc
from VizTyping.meta.object_meta import VizorObjectMetaDoc, VizorRectParamsDoc, \
    VizorKpsParamsDoc, VizorMaskParamsDoc, VizorKpsType, VizorKpsDoc
from VizTyping.meta.label_info import VizorLabelInfoMetaDoc
from docarray import BaseDoc

from enum import Enum
from typing import Optional, List

__all__ = ['RmInferTaskDoc', 'RmTrainTaskDoc', 'AddTrainTaskDoc', 'AddInferTaskDoc', 'StopInferModelDoc',
           'StartInferModelDoc', 'VizorBackendTypeDoc', 'VizorBackendStatusDoc', 'VizorBackendInfoDoc',
           'RegisterDoc', 'ResponseDoc', 'InferModelInfoDoc', 'InferTaskInfoDoc', "InferModelStatus",
           "FlowControllerRet", "VizorFrameMetaDoc", "VizorClassifierMetaDoc", "VizorObjectMetaDoc",
           "VizorLabelInfoMetaDoc", "RouteNodeInferTaskDoc", "V2NAddInferTaskDoc", "VizorRectParamsDoc",
           "VizorKpsParamsDoc", "VizorMaskParamsDoc", "VizorKpsType", "VizorKpsDoc", "InferTaskRouteDoc",
           "TrainTaskInfoDoc", "ParametersDoc", "N2VResponseDoc"]


class ResponseDoc(BaseDoc):
    success: bool
    errCode: int
    errMessage: str


class N2VResponseDoc(BaseDoc):
    success: bool
    errCode: int
    errMessage: str
    BSLs: Optional[List[VizorBackendInfoDoc]] = None


class FlowControllerRet(Enum):
    MODEL_FILE_NOT_EXIST = 0





