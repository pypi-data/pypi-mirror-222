from docarray import BaseDoc
from typing import List
from .label_info import VizorLabelInfoMetaDoc


class VizorClassifierMetaDoc(BaseDoc):
    numLabels: int = None
    labelInfoList: List[VizorLabelInfoMetaDoc]
