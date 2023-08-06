from docarray import BaseDoc
from docarray.typing import ImageTensor
from typing import List, Optional
from .object_meta import VizorObjectMetaDoc
from .classifier_meta import VizorClassifierMetaDoc


class VizorFrameMetaDoc(BaseDoc):
    """
    图像/帧元数据， 包含图像/帧的基本信息，包括图像/帧的宽高，帧率，以及图像/帧中的目标和分类器信息，
    目标结构中嵌套了分类器结构，目标和分类器结构中都包含了标签信息， 只有两层，不会再嵌套了， 如果有需要后续再修改，
    应对的情况就是， 检测到某个对象对其进行分类，观察其属性， 如果满足再进行某种类型的检测，比如人脸检测，人脸检测后再进行人脸属性检测
    如此嵌套
    """
    taskId: str
    # Path of source
    dataPath: str
    # Current frame number of source
    frameNum: Optional[int]
    # List of objects of type VizorObjectMetaDoc in usr for give frame
    objMetaList: Optional[List[VizorObjectMetaDoc]]
    # List of classifiers of type VizorClassifierMetaDoc in usr for give frame
    classifierMetaList: Optional[List[VizorClassifierMetaDoc]]
    #  Holds the width of the frame after decode
    sourceFrameWidth: Optional[int]
    # Holds the height of the frame after decode
    sourceFrameHeight: Optional[int]
    # Holds the frame rate of the source
    sourceFrameFps: Optional[float]
    # Holds the frame data of the source
    surfaceData: Optional[ImageTensor]

