from typing import TypedDict, Annotated
from operator import add

class State(TypedDict):
    notes: str
    participants: list[str]
    topics: list[str]
    action_items: list[str]
    minutes: str
    summary: str
    logs: Annotated[list[str],add]
    
    