from docarray import BaseDoc
from backend.type import VizorBackendTypeDoc


class RegisterDoc(BaseDoc):
    backendName: str = None
    backendType: str = None
    backendIp: str = None
    backendPort: int = None
    forceRegister: bool = False
