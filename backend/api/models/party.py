# backend/api/models/party.py
"""
SQLAlchemy model for the Party table.
Represents a political party in the database, including its name and platform.
"""

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base


class Party(Base):
    """
    Represents a political party in the database.

    Attributes:
        id (int): Primary key, unique identifier for the party.
        name (str): Name of the political party (e.g., 'Liberal', 'Conservative').
        platform (str): Text describing the party's platform and key positions.
        created_at (datetime): Timestamp when the party record was created.
    """
    __tablename__ = "parties"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    platform = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Define relationship to Politician for easier querying
    # Note: Uncomment this if you add back_populates to Politician model
    # politicians = relationship("Politician", back_populates="party")