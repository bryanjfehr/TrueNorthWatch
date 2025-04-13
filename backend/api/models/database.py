# backend/api/models/database.py
"""
Centralized SQLAlchemy base for all models.
"""
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()