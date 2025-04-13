# backend/api/models/vote.py
"""
SQLAlchemy model for the Vote table.
"""

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from .database import Base

class Vote(Base):
    """
    Represents a vote cast by a politician on a bill.

    Attributes:
        id (int): Primary key.
        politician_id (int): Foreign key to Politician.
        bill_id (int): Foreign key to Bill.
        vote (str): Vote cast ('yes', 'no', 'abstain').
        created_at (datetime): Timestamp when the vote was recorded.
    """
    __tablename__ = "votes"
    id = Column(Integer, primary_key=True, index=True)
    politician_id = Column(Integer, ForeignKey("politicians.id"), nullable=False)
    bill_id = Column(Integer, ForeignKey("bills.id"), nullable=False)
    vote = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)