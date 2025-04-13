# backend/api/models/politician.py
"""
SQLAlchemy model for the Politician table.
"""

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from .database import Base

class Politician(Base):
    """
    Represents a politician in the database.

    Attributes:
        id (int): Primary key.
        name (str): Full name of the politician.
        party_id (int): Foreign key to the Party table.
        position (str): Current role or position (e.g., MP, Minister).
        created_at (datetime): Timestamp when the record was created.
    """
    __tablename__ = "politicians"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    party_id = Column(Integer, ForeignKey("parties.id"), nullable=False)
    position = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Optional: Define relationships for easier querying
    # party = relationship("Party", back_populates="politicians")