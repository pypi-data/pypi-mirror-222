from docarray import BaseDoc
from enum import Enum
from typing import Optional, Dict, List
from VizTyping.backend.info import VizorBackendInfoDoc
"""
添加推理任务
{
    "taskId": 121,
    "current": 0,
    "dataPath": "rtsp://admin:admin123@172.31.100.59:554/cam/realmonitor?channel=2&subtype=0",
    "videoStreamId": "1",
    "space": "1",
    "type": "relDetectVideo",
    "merge": true,
    "route": {
    //// 步骤序号 "1" / "2" / "3" / "4"
    "1": {
      //// versionId
      "200": {
        // 阈值，本地视频，组织视频使用
        "threshold": 0.3,
        // 模型名称
        "modelName": "yolov5_5m",
        // 是否返回平台
        "save": true,
        // 必有字段，串行时需要用到，并行时给空对象 {} 即可
        "next_stage": {}
      },
      "201": {
        // 阈值，本地视频，组织视频使用
        "threshold": 0.3,
        // 模型类型
        "modelName": "yolov5_5m",
        // 是否返回
        "save": true,
        "next_stage": {}
      }
    }
  }
}
"""


class InferTaskTypeDoc(Enum):
    DETECT_IMAGE = "detectImage"
    CLASS_IMAGE = "classImage"
    DETECT_VIDEO = "detectVideo"
    CLASS_VIDEO = "classVideo"
    REL_DETECT_VIDEO = "relDetectVideo"


class InferTaskRouteDoc(BaseDoc):
    threshold: int
    modelName: str
    save: bool
    next_stage: Dict


class AddInferTaskDoc(BaseDoc):
    taskId: int
    current: int
    dataPath: str
    type: InferTaskTypeDoc
    videoStreamId: Optional[str]
    space: Optional[str]
    merge: bool
    route: Dict[str, Dict[str, InferTaskRouteDoc]]


class RouteNodeInferTaskDoc(BaseDoc):
    versionId: str
    backendName: str
    backendIp: str
    backendPort: int
    backendModelVersionId: int
    threshold: int
    modelName: str
    save: bool
    nextStageVersionIds: Optional[List[str]]
    inputLabelList: Optional[List[str]]


class V2NAddInferTaskDoc(BaseDoc):
    """
    推理结点任务分发请求结构， 用于推理结点任务分发和位于同一DAG计算图中的推理任务数据传递
    """
    # 当前推理任务ID，用于BSL结点判断接收到的是否属于同一推理任务，进行推理结果合并
    taskId: int
    # 指定模型输出的结果的阈值，用于过滤模型输出的结果
    threshold: float
    # 模型名称， 暂时没有什么用途， 有versionId已经可以实现模型的唯一标识
    modelName: str
    # 是否将推理结果保存到平台
    save: bool
    # 数据地址，当推理任务的类型为视频时，该地址没有实质作用， 只有第一个结点才会进行使用该地址进行推理， 剩余的结点
    # 使用上一个结点通过FrameMeta传递的数据进行推理
    dataPath: str
    # 当前推理结点的backend框架内运行的模型versionId， 唯一标识
    versionId: str
    # 本次推理任务的类型
    type: InferTaskTypeDoc
    # 视频流ID
    videoStreamId: Optional[str]
    # 视频的抽帧间隔， 一秒抽多少帧
    space: Optional[str]
    # 是否需要合并推理结果
    merge: bool
    # 当前推理任务的输入标签列表， 用于过滤模型输入的标签
    inputLabelList: Optional[List[str]] = None
    # 上一阶段推理任务的versionId， 用于推理结点任务分发, 可选
    previousStageVersionIds: Optional[List[str]] = None
    # 当前推理任务的下一个推理结点的versionId， 用于推理结点任务分发, 可选
    nextStageVersionIds: Optional[List[str]] = None
    # 当前推理任务的下一个推理结点的推理任务信息，使用versionId作为key, 可选
    routeNodeInferInfos: Optional[Dict[str, RouteNodeInferTaskDoc]] = None


class InferTaskInfoDoc(BaseDoc):
    inputNodeBackendInfos:  Dict[str, VizorBackendInfoDoc] = None
    taskInfos: List[V2NAddInferTaskDoc] = None



