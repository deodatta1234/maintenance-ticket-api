from enum import StrEnum

from pydantic import BaseModel


class Priority(StrEnum):
    low = "low"
    medium = "medium"
    high = "high"


class MaintenanceTicket(BaseModel):
    id: int
    title: str
    priority: Priority
