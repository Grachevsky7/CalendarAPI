import model
import storage_interface
from datetime import datetime

DATE_LIMIT = 10
TITLE_LIMIT = 30
TEXT_LIMIT = 200


class LogicException(Exception):
    pass


class EventLogic:
    def __init__(self):
        self._event_SI = storage_interface.EventSI()


    @staticmethod
    def _validate_event(event: model.Event, date_control=datetime.now().date(), date_list=[]):
        if event is None:
            raise LogicException("event is None")
        if event.date is None or len(event.date) > DATE_LIMIT:
            raise LogicException(f"date length > MAX: {DATE_LIMIT}")
        if datetime.strptime(event.date, '%Y-%m-%d') is False:
            raise LogicException(f"Incorrect input: {event.date}")
        if event.title is None or len(event.title) > TITLE_LIMIT:
            raise LogicException(f"title length > MAX: {TITLE_LIMIT}")
        if event.text is None or len(event.text) > TEXT_LIMIT:
            raise LogicException(f"text length > MAX: {TEXT_LIMIT}")
        #if date_control not in date_list: date_list.append(date_control)
        #else:
        #   raise LogicException(f"Limit input: one in {event.date}")

    def create(self, event: model.Event) -> str:
        self._validate_event(event)
        try:
            return self._event_SI.create(event)
        except Exception as ex:
            raise LogicException(f"failed CREATE operation with: {ex}")

    def list(self) -> list[model.Event]:
        try:
            return self._event_SI.list()
        except Exception as ex:
            raise LogicException(f"failed LIST operation with: {ex}")

    def read(self, _id: str) -> model.Event:
        try:
            return self._event_SI.read(_id)
        except Exception as ex:
            raise LogicException(f"failed READ operation with: {ex}")

    def update(self, _id: str, event: model.Event):
        self._validate_event(event)
        try:
            return self._event_SI.update(_id, event)
        except Exception as ex:
            raise LogicException(f"failed UPDATE operation with: {ex}")

    def delete(self, _id: str):
        try:
            return self._event_SI.delete(_id)
        except Exception as ex:
            raise LogicException(f"failed DELETE operation with: {ex}")