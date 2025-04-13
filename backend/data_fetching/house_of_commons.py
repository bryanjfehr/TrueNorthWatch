# backend/api/data_fetching/house_of_commons.py
"""
Module for fetching bills and votes from the House of Commons.
Supports fetching data from Open Parliament API or scraping the Parliament website.
"""

import requests
from typing import List, Dict, Optional
from datetime import datetime


def fetch_bills(start_year: int = 2006) -> List[Dict]:
    """
    Fetch bills introduced in the House of Commons since the specified year.

    Args:
        start_year (int): Year to start fetching bills from (default: 2006).

    Returns:
        List[Dict]: List of bill details, each containing:
            - 'id': Bill identifier
            - 'title': Bill title
            - 'description': Bill description
            - 'status': Current status
            - 'introduced_by': Politician ID (placeholder)
            - 'created_at': Timestamp
    """
    base_url = "https://openparliament.ca/api/bills/"  # Placeholder API endpoint
    bills = []

    try:
        # Placeholder: Fetch bills from API
        response = requests.get(base_url, params={"year__gte": start_year}, timeout=10)
        response.raise_for_status()
        raw_bills = response.json()

        for bill in raw_bills:
            bills.append({
                "id": bill.get("id", 0),
                "title": bill.get("title", "Unknown"),
                "description": bill.get("description", "No description"),
                "status": bill.get("status", "proposed"),
                "introduced_by": bill.get("sponsor_id", 1),  # Placeholder
                "created_at": datetime.utcnow().isoformat()
            })

    except requests.RequestException as e:
        print(f"Error fetching bills: {e}")
        # Return dummy data for testing
        bills.append({
            "id": 1,
            "title": "Sample Bill",
            "description": "A sample bill for testing",
            "status": "proposed",
            "introduced_by": 1,
            "created_at": datetime.utcnow().isoformat()
        })

    return bills


def fetch_votes(bill_id: Optional[int] = None) -> List[Dict]:
    """
    Fetch votes cast on bills in the House of Commons.

    Args:
        bill_id (Optional[int]): ID of the bill to fetch votes for. If None,
            fetches all available votes.

    Returns:
        List[Dict]: List of vote details, each containing:
            - 'id': Vote identifier
            - 'politician_id': ID of the politician who voted
            - 'bill_id': ID of the bill
            - 'vote': Vote cast ('yes', 'no', 'abstain')
            - 'created_at': Timestamp
    """
    base_url = "https://openparliament.ca/api/votes/"  # Placeholder API endpoint
    votes = []

    try:
        params = {"bill_id": bill_id} if bill_id else {}
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        raw_votes = response.json()

        for vote in raw_votes:
            votes.append({
                "id": vote.get("id", 0),
                "politician_id": vote.get("politician_id", 1),  # Placeholder
                "bill_id": vote.get("bill_id", bill_id or 1),
                "vote": vote.get("vote", "yes"),
                "created_at": datetime.utcnow().isoformat()
            })

    except requests.RequestException as e:
        print(f"Error fetching votes: {e}")
        # Return dummy data for testing
        votes.append({
            "id": 1,
            "politician_id": 1,
            "bill_id": bill_id or 1,
            "vote": "yes",
            "created_at": datetime.utcnow().isoformat()
        })

    return votes


# Example usage:
# if __name__ == "__main__":
#     bills = fetch_bills(start_year=2006)
#     votes = fetch_votes(bill_id=1)
#     print(bills)
#     print(votes)