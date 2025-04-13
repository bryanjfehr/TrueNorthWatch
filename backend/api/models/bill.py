# backend/api/models/bill.py
"""
SQLAlchemy model for the Bill table.
"""

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# Note: Base should ideally be defined in a central file (e.g., database.py)
Base = declarative_base()

class Bill(Base):
    """
    Represents a bill in the House of Commons.

    Attributes:
        id (int): Primary key.
        title (str): Title of the bill.
        description (str): Detailed description of the bill.
        status (str): Current status (e.g., 'proposed', 'passed').
        introduced_by (int): Foreign key to the Politician who introduced the bill.
        created_at (datetime): Timestamp when the record was created.
    """
    __tablename__ = "bills"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    status = Column(String, nullable=False)
    introduced_by = Column(Integer, ForeignKey("politicians.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Optional: Define relationships for easier querying
    # introduced_by_politician = relationship("Politician", back_populates="bills")