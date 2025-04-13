# backend/api/models/schemas.py
"""
Pydantic schemas for API data validation and serialization.
These schemas define the structure of data exchanged between the frontend and backend,
ensuring type safety and proper serialization of SQLAlchemy models.
"""

from pydantic import BaseModel
from datetime import datetime

class PartySchema(BaseModel):
    """
    Schema representing a political party.

    Attributes:
        id (int): Unique identifier for the party.
        name (str): Name of the political party.
        created_at (datetime): Timestamp when the party was added to the database.
    """
    id: int
    name: str
    created_at: datetime

    class Config:
        orm_mode = True

class PlatformCategorySchema(BaseModel):
    """
    Schema representing a categorized stance of a political party's platform.

    Attributes:
        id (int): Unique identifier for the category stance.
        party_id (int): Foreign key to the Party table.
        election_year (int): Year of the election campaign.
        category (str): Category of the stance (e.g., 'Climate Change and Energy').
        stance (str): Text describing the party's stance in that category.
        created_at (datetime): Timestamp when the record was created.
    """
    id: int
    party_id: int
    election_year: int
    category: str
    stance: str
    created_at: datetime

    class Config:
        orm_mode = True

class PoliticianSchema(BaseModel):
    """
    Schema representing a politician.

    Attributes:
        id (int): Unique identifier for the politician.
        name (str): Full name of the politician.
        party_id (int): Foreign key referencing the Party table (many-to-one).
        position (str): Current role or position (e.g., MP, Minister).
        created_at (datetime): Timestamp when the politician was added.
    """
    id: int
    name: str
    party_id: int
    position: str
    created_at: datetime

    class Config:
        orm_mode = True

class BillSchema(BaseModel):
    """
    Schema representing a bill introduced in the House of Commons.

    Attributes:
        id (int): Unique identifier for the bill.
        title (str): Title of the bill.
        description (str): Detailed text of the bill, used for semantic analysis.
        status (str): Current status (e.g., 'proposed', 'passed', 'rejected').
        introduced_by (int): Foreign key referencing the Politician who introduced it.
        created_at (datetime): Timestamp when the bill was added.
    """
    id: int
    title: str
    description: str
    status: str
    introduced_by: int
    created_at: datetime

    class Config:
        orm_mode = True

class VoteSchema(BaseModel):
    """
    Schema representing a vote cast by a politician on a bill.

    Attributes:
        id (int): Unique identifier for the vote.
        politician_id (int): Foreign key referencing the Politician (many-to-one).
        bill_id (int): Foreign key referencing the Bill (many-to-one).
        vote (str): The vote cast (e.g., 'yes', 'no', 'abstain').
        created_at (datetime): Timestamp when the vote was recorded.
    """
    id: int
    politician_id: int
    bill_id: int
    vote: str
    created_at: datetime

    class Config:
        orm_mode = True