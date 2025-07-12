from typing import Optional
from pydantic import BaseModel

# Base schema shared by create and response models
class TicketBase(BaseModel):
    title: str
    amount: Optional[float] = None
    destination: Optional[str] = None

# Schema for creating a new ticket
class TicketCreate(TicketBase):
    pass

# Schema for returning ticket details
class Ticket(TicketBase):
    id: int

    class Config:
        orm_mode = True
