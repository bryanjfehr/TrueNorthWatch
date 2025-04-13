# backend/api/models/party.py
"""
SQLAlchemy model for the Party and PlatformCategory tables.
Represents a political party and its categorized platform stances in the database.
"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class Party(Base):
    """
    Represents a political party in the database.

    Attributes:
        id (int): Primary key, unique identifier for the party.
        name (str): Name of the political party (e.g., 'Liberal', 'Conservative').
        created_at (datetime): Timestamp when the party record was created.
    """
    __tablename__ = "parties"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship to PlatformCategory
    platform_categories = relationship("PlatformCategory", back_populates="party")

class PlatformCategory(Base):
    """
    Represents a categorized stance of a political party's platform for a specific election year.

    Attributes:
        id (int): Primary key.
        party_id (int): Foreign key to the Party table.
        election_year (int): Year of the election campaign.
        category (str): Category of the stance (e.g., 'Climate Change and Energy').
        stance (str): Text describing the party's stance in that category.
        created_at (datetime): Timestamp when the record was created.
    """
    __tablename__ = "platform_categories"

    id = Column(Integer, primary_key=True, index=True)
    party_id = Column(Integer, ForeignKey("parties.id"), nullable=False)
    election_year = Column(Integer, nullable=False)
    category = Column(String, nullable=False)
    stance = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship to Party
    party = relationship("Party", back_populates="platform_categories")