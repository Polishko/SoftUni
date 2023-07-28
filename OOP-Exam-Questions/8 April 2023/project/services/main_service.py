from project.services.base_service import BaseService


class MainService(BaseService):
    _CAPACITY = 30
    _TYPE = "Main Service"
    
    def __init__(self, name: str):
        super().__init__(name, capacity=self._CAPACITY)

    @property
    def service_type(self):
        return self._TYPE
