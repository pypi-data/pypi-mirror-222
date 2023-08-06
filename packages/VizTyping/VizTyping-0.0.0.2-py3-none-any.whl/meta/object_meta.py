from docarray import BaseDoc
from docarray.typing import NdArray
from .classifier_meta import VizorClassifierMetaDoc
from enum import Enum
from typing import List, Optional


class VizorRectParamsDoc(BaseDoc):
    top: float
    left: float
    width: float
    height: float


class VizorMaskParamsDoc(BaseDoc):
    threshold: float
    width: int
    height: int
    data: NdArray


class VizorKpsDoc(BaseDoc):
    """
    关键点， 包括关键点的id， 关键点的类型， 位置信息`
    """
    kpsId: int
    kpsLabel: str
    top: float
    left: float


class VizorKpsType(Enum):
    """
    关键点类型
    """
    FACE = "FACE"
    BODY = "BODY"
    HAND = "HAND"


class VizorKpsParamsDoc(BaseDoc):
    """
    关键点参数， 包括关键点的id， 关键点的类型， 位置信息
    """
    data: List[VizorKpsDoc]
    kpsNum: int
    kpsType: VizorKpsType


class VizorObjectMetaDoc(BaseDoc):
    classId: Optional[int]
    objectId: Optional[int]
    confidence: Optional[float]
    rectParams: Optional[VizorRectParamsDoc]
    kpsParams: Optional[VizorKpsParamsDoc]
    maskParams: Optional[VizorMaskParamsDoc]
    objLabel: Optional[str]
    objVector: Optional[NdArray]
    classifier_meta_list: Optional[List[VizorClassifierMetaDoc]]

