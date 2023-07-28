from project.services.base_service import BaseService


class SecondaryService(BaseService):
    _CAPACITY = 15
    _TYPE = "Secondary Service"

    def __init__(self, name: str):
        super().__init__(name, capacity=self._CAPACITY)

    @property
    def service_type(self):
        return self._TYPE
