# backend/api/routes/data.py
"""
API routes for fetching data on politicians, bills, votes, and party platforms.
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from api.models.database import get_db
from api.models.party import Party, PlatformCategory
from api.data_fetching.party_platforms import fetch_party_platform
from api.data_processing.categorize_platform import categorize_text
from api.data_processing.analyze_stance import analyze_stance
from api.models.schemas import PoliticianSchema, BillSchema, VoteSchema, PlatformCategorySchema

router = APIRouter()

@router.get("/politicians", response_model=list[PoliticianSchema])
def get_politicians():
    """
    Fetch a list of politicians.
    TODO: Replace with actual database query.
    """
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
    return [
        {"id": 1, "title": "Bill A", "description": "Description A", "status": "proposed", "introduced_by": 1, "created_at": "2023-01-03T00:00:00"}
    ]

@router.get("/votes", response_model=list[VoteSchema])
def get_votes():
    """
    Fetch a list of votes.
    TODO: Replace with actual database query.
    """
    return [
        {"id": 1, "politician_id": 1, "bill_id": 1, "vote": "yes", "created_at": "2023-01-04T00:00:00"}
    ]

@router.get("/parties/{party_id}/platforms/{election_year}", response_model=list[PlatformCategorySchema])
def get_party_platform_categories(party_id: int, election_year: int, db: Session = Depends(get_db)):
    """
    Fetch and categorize the platform for a specific party and election year.

    Args:
        party_id (int): ID of the party.
        election_year (int): Year of the election campaign.
        db (Session): Database session dependency.

    Returns:
        list[PlatformCategorySchema]: List of categorized stances for the party in that election year.
    """
    # Check if categories already exist in the database
    existing_categories = db.query(PlatformCategory).filter(
        PlatformCategory.party_id == party_id,
        PlatformCategory.election_year == election_year
    ).all()

    if existing_categories:
        return existing_categories

    # Fetch party details
    party = db.query(Party).filter(Party.id == party_id).first()
    if not party:
        return {"error": "Party not found"}

    # Fetch platform text
    platform_data = fetch_party_platform(party.name, election_year)
    platform_text = platform_data["platform"]

    # Categorize the text into the 15 categories
    categorized = categorize_text(platform_text)

    # Analyze sentiment to determine stances
    stances = analyze_stance(categorized)

    # Store in database
    for category, stance in stances.items():
        db_category = PlatformCategory(
            party_id=party_id,
            election_year=election_year,
            category=category,
            stance=stance,
            created_at=datetime.utcnow()
        )
        db.add(db_category)

    db.commit()

    # Return the newly created categories
    new_categories = db.query(PlatformCategory).filter(
        PlatformCategory.party_id == party_id,
        PlatformCategory.election_year == election_year
    ).all()
    return new_categories