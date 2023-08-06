from docarray import BaseDoc


class RmTrainTaskDoc(BaseDoc):
    versionId: int
    operation: str
