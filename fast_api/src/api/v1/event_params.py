from dataclasses import dataclass

from fastapi import Query


@dataclass
class EventParams:
    topic: str = Query(default='')
    value: str = Query(default='')
    key:   str = Query(default='')


def get_event_params():
    return EventParams
