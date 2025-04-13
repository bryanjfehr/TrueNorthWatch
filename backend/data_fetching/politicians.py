# backend/api/data_fetching/politicians.py
"""
Module for fetching politician data.
Supports fetching current and historical politicians from Parliament or other sources.
"""

import requests
from typing import List, Dict, Optional
from datetime import datetime


def fetch_politicians(start_year: int = 2006) -> List[Dict]:
    """
    Fetch politicians who served since the specified year.

    Args:
        start_year (int): Year to start fetching politicians from (default: 2006).

    Returns:
        List[Dict]: List of politician details, each containing:
            - 'id': Politician identifier
            - 'name': Full name
            - 'party_id': ID of the party (placeholder)
            - 'position': Current role (e.g., 'MP', 'Minister')
            - 'created_at': Timestamp
    """
    base_url = "https://openparliament.ca/api/politicians/"  # Placeholder API endpoint
    politicians = []

    try:
        response = requests.get(base_url, params={"year__gte": start_year}, timeout=10)
        response.raise_for_status()
        raw_politicians = response.json()

        for pol in raw_politicians:
            politicians.append({
                "id": pol.get("id", 0),
                "name": pol.get("name", "Unknown"),
                "party_id": pol.get("party_id", 1),  # Placeholder
                "position": pol.get("position", "MP"),
                "created_at": datetime.utcnow().isoformat()
            })

    except requests.RequestException as e:
        print(f"Error fetching politicians: {e}")
        # Return dummy data for testing
        politicians.append({
            "id": 1,
            "name": "John Doe",
            "party_id": 1,
            "position": "MP",
            "created_at": datetime.utcnow().isoformat()
        })

    return politicians


# Example usage:
# if __name__ == "__main__":
#     politicians = fetch_politicians(start_year=2006)
#     print(politicians)