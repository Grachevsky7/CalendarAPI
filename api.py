from flask import Flask
from flask import request
import model
import logic

app = Flask(__name__)

_event_logic = logic.EventLogic()
class ApiException(Exception):
    pass

def _from_raw(raw_event:str) -> model.Event:
    parts = raw_event.split('|')
    if len(parts) == 3:
        event = model.Event()
        event.id = None
        event.date = parts[0]
        event.title = parts[1]
        event.text = parts[2]
        return event
    elif len(parts) == 4:
        event = model.Event()
        event.id = parts[0]
        event.date = parts[1]
        event.title = parts[2]
        event.text = parts[3]
        return event
    else:
        raise ApiException(f'Invalid RAW event data {raw_event}')

def _to_raw(event: model.Event) -> str:
    if event.id is None:
        return f"{event.date}|{event.title}|{event.text}"
    else:
        return f"{event.id}|{event.date}|{event.title}|{event.text}"

API_ROOT = '/api/v1/'
CALENDAR_API = API_ROOT + 'calendar/'


@app.route(CALENDAR_API, methods=['POST'])
def create():
    try:
        data = request.get_data().decode('utf-8')
        event = _from_raw(data)
        _id = _event_logic.create(event)
        return {'create status': 'success', 'result': f'{event.id}|{event.date}|{event.title}|{event.text}'}, 201
    except Exception as ex:
        return f'failed to CREATE with {ex}', 404

@app.route(CALENDAR_API, methods=['GET'])
def list():
    try:
        events = _event_logic.list()
        raw_events = ""
        for event in events:
            raw_events += _to_raw(event) + '\n'
        return raw_events, 200
    except Exception as ex:
        return f"failed to LIST with: {ex}", 404

@app.route(CALENDAR_API + '<_id>', methods=['GET'])
def read(_id: str):
    try:
        event = _event_logic.read(_id)
        raw_event = _to_raw(event)
        return {'read status': 'success', 'result': f'{raw_event}'}, 200
    except Exception as ex:
        return f'failed to READ with: {ex}', 404

@app.route(CALENDAR_API + '<_id>', methods=['PUT'])
def update(_id: str):
    try:
        data = request.get_data().decode('utf-8')
        event = _from_raw(data)
        _event_logic.update(_id, event)
        return {'update status': 'success'}, 200
    except Exception as ex:
        return f"failed to UPDATE with: {ex}", 404

@app.route(CALENDAR_API + '<_id>', methods=['DELETE'])
def delete(_id: str):
    try:
        _event_logic.delete(_id)
        return {'delete status': 'success'}, 200
    except Exception as ex:
        return f"failed to DELETE with: {ex}", 404

app.run()
