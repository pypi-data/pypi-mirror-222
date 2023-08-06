from docarray import BaseDoc
from .type import VizorBackendTypeDoc
from .status import VizorBackendStatusDoc


class VizorBackendInfoDoc(BaseDoc):
    backendStatus: VizorBackendStatusDoc = None
    backendType: VizorBackendTypeDoc = None
    backendName: str
    backendIp: str
    backendPort: int
