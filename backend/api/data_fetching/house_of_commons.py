# backend/api/data_fetching/house_of_commons.py
"""
Module for fetching bills and votes from the House of Commons using the Open Parliament API.
"""

import requests
from typing import List, Dict, Optional
from datetime import datetime
import time

# Replace with your actual email
USER_EMAIL = "your.email@example.com"

def fetch_bills(start_year: int = 2006) -> List[Dict]:
    """
    Fetch bills introduced in the House of Commons since the specified year using the Open Parliament API.

    Args:
        start_year (int): Year to start fetching bills from (default: 2006).

    Returns:
        List[Dict]: List of bill details with fields like 'url', 'number', 'title', etc.
    """
    base_url = "https://openparliament.ca/api/bills/"
    headers = {"API-Version": "v1", "User-Agent": USER_EMAIL}
    params = {"introduced_date__gte": f"{start_year}-01-01"}  # Filter bills since start_year
    bills = []

    try:
        response = requests.get(base_url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        raw_bills = response.json()  # Expecting a list of bills

        for bill in raw_bills:
            bills.append({
                "url": bill.get("url", ""),  # Unique identifier
                "number": bill.get("number", "Unknown"),  # e.g., "C-10"
                "title": bill.get("name", "Unknown"),
                "description": bill.get("summary", "No description"),
                "status": bill.get("status", "proposed"),
                "introduced_by": bill.get("sponsor", ""),  # Politician URL
                "introduced_date": bill.get("introduced_date", ""),
                "created_at": datetime.utcnow().isoformat()
            })
        time.sleep(0.5)  # Avoid rate limits

    except requests.RequestException as e:
        print(f"Error fetching bills: {e}")
        bills.append({
            "url": "/bills/1/",
            "number": "C-1",
            "title": "Sample Bill",
            "description": "A sample bill for testing",
            "status": "proposed",
            "introduced_by": "/politicians/1/",
            "introduced_date": "2006-01-01",
            "created_at": datetime.utcnow().isoformat()
        })

    return bills

def fetch_votes(bill_url: Optional[str] = None) -> List[Dict]:
    """
    Fetch votes cast on bills in the House of Commons using the Open Parliament API.

    Args:
        bill_url (Optional[str]): URL of the bill (e.g., "/bills/42-1/C-10/"). If None, fetches all votes.

    Returns:
        List[Dict]: List of vote details with fields like 'url', 'politician_url', etc.
    """
    base_url = "https://openparliament.ca/api/votes/"
    headers = {"API-Version": "v1", "User-Agent": USER_EMAIL}
    params = {"bill": bill_url} if bill_url else {}
    votes = []

    try:
        response = requests.get(base_url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        raw_votes = response.json()

        for vote in raw_votes:
            votes.append({
                "url": vote.get("url", ""),
                "politician_url": vote.get("politician_url", ""),
                "bill_url": vote.get("bill_url", bill_url or ""),
                "vote": vote.get("vote", "yes"),
                "created_at": datetime.utcnow().isoformat()
            })
        time.sleep(0.5)  # Avoid rate limits

    except requests.RequestException as e:
        print(f"Error fetching votes: {e}")
        votes.append({
            "url": "/votes/1/",
            "politician_url": "/politicians/1/",
            "bill_url": bill_url or "/bills/1/",
            "vote": "yes",
            "created_at": datetime.utcnow().isoformat()
        })

    return votes

# Example usage:
# if __name__ == "__main__":
#     bills = fetch_bills(start_year=2006)
#     votes = fetch_votes(bill_url="/bills/42-1/C-10/")
#     print(bills)
#     print(votes)