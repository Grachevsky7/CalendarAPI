import model
import storage

class SIException(Exception):
    pass

class EventSI:
    def __init__(self):
        self._storage = storage.LocalStorage()

    def create(self, event: model.Event) -> str:
        try:
            return self._storage.create(event)
        except Exception as ex:
            raise SIException(f"failed CREATE operation with: {ex}")

    def list(self) -> list[model.Event]:
        try:
            return self._storage.list()
        except Exception as ex:
            raise SIException(f"failed LIST operation with: {ex}")

    def read(self, _id: str) -> model.Event:
        try:
            return self._storage.read(_id)
        except Exception as ex:
            raise SIException(f"failed READ operation with: {ex}")

    def update(self, _id: str, event: model.Event):
        try:
            return self._storage.update(_id, event)
        except Exception as ex:
            raise SIException(f"failed UPDATE operation with: {ex}")

    def delete(self, _id: str):
        try:
            return self._storage.delete(_id)
        except Exception as ex:
            raise SIException(f"failed DELETE operation with: {ex}")