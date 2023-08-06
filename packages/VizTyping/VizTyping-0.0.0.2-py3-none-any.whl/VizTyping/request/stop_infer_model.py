from docarray import BaseDoc


class StopInferModelDoc(BaseDoc):
    versionId: int
    operation: str
