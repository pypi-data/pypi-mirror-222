from docarray import BaseDoc
from typing import List


class VizorLabelInfoMetaDoc(BaseDoc):
    numClasses: int
    labels: List[str]
    labelId: int
