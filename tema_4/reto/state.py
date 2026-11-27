from typing import TypedDict

class State(TypedDict):
    notes: str
    participants: list[str]
    topics: list[str]
    action_items: list[str]
    minutes: str
    summary: str
    
    