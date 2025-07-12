from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base

# Ticket model for the database
class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    amount = Column(Float, nullable=True)
    destination = Column(String(255), nullable=True)

