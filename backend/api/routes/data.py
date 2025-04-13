# backend/api/routes/data.py
"""
API routes for fetching data on politicians, bills, and votes.
"""

from fastapi import APIRouter
from api.models.schemas import PoliticianSchema, BillSchema, VoteSchema

router = APIRouter()

@router.get("/politicians", response_model=list[PoliticianSchema])
def get_politicians():
    """
    Fetch a list of politicians.
    TODO: Replace with actual database query.
    """
    # Dummy data for testing
    return [
        {"id": 1, "name": "John Doe", "party_id": 1, "position": "MP", "created_at": "2023-01-01T00:00:00"},
        {"id": 2, "name": "Jane Smith", "party_id": 2, "position": "Minister", "created_at": "2023-01-02T00:00:00"}
    ]

@router.get("/bills", response_model=list[BillSchema])
def get_bills():
    """
    Fetch a list of bills.
    TODO: Replace with actual database query.
    """
    # Dummy data for testing
    return [
        {"id": 1, "title": "Bill A", "description": "Description A", "status": "proposed", "introduced_by": 1, "created_at": "2023-01-03T00:00:00"}
    ]

@router.get("/votes", response_model=list[VoteSchema])
def get_votes():
    """
    Fetch a list of votes.
    TODO: Replace with actual database query.
    """
    # Dummy data for testing
    return [
        {"id": 1, "politician_id": 1, "bill_id": 1, "vote": "yes", "created_at": "2023-01-04T00:00:00"}
    ]