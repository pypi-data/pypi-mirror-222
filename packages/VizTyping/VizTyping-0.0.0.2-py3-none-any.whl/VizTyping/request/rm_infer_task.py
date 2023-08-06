from docarray import BaseDoc


class RmInferTaskDoc(BaseDoc):
    """
    该操作仅针对视频， 图片的推理无法移除
    """
    taskId: int
    type: str

