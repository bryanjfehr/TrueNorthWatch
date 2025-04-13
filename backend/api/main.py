# backend/api/main.py (updated)
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.models.database import Base

app = FastAPI(
    title="TrueNorthWatch API",
    description="API for tracking politician integrity and bill analysis in Canada.",
    version="0.1.0"
)

# Database connection (update with your credentials)
DATABASE_URL = "postgresql://user:password@localhost:5432/truenorthwatch"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Create tables
Base.metadata.create_all(bind=engine)