from sqlalchemy.orm import Session
from app.db.models import Ticket
from app.schemas.ticket_schema import TicketCreate
from typing import List, Optional

# Get all tickets
def get_all_tickets(db: Session) -> List[Ticket]:
    return db.query(Ticket).all()

# Retrieve a single ticket by its ID
def get_ticket(db: Session, ticket_id: int) -> Optional[Ticket]:
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()

# Create a new ticket
def create_ticket(db: Session, ticket_data: TicketCreate) -> Ticket:
    new_ticket = Ticket(
        title=ticket_data.title,
        amount=ticket_data.amount,
        destination=ticket_data.destination
    )
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket

# Update an existing ticket by ID
def update_ticket(db: Session, ticket_id: int, ticket_data: TicketCreate) -> Optional[Ticket]:
    ticket = get_ticket(db, ticket_id)
    if ticket:
        ticket.title = ticket_data.title
        ticket.amount = ticket_data.amount
        ticket.destination = ticket_data.destination
        db.commit()
        db.refresh(ticket)
    return ticket

# Delete a ticket by ID
def delete_ticket(db: Session, ticket_id: int) -> bool:
    ticket = get_ticket(db, ticket_id)
    if not ticket:
        return False
    db.delete(ticket)
    db.commit()
    return True
