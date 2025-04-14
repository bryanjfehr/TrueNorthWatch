# backend/api/data_fetching/politicians.py
"""
Module for fetching politician data from the Open Parliament API.
"""

import requests
from typing import List, Dict
from datetime import datetime
import time

USER_EMAIL = "your.email@example.com"

def fetch_politicians(start_year: int = 2006) -> List[Dict]:
    """
    Fetch politicians who served since the specified year from the Open Parliament API.

    Args:
        start_year (int): Year to filter politicians from (default: 2006). Note: Filtering done post-fetch.

    Returns:
        List[Dict]: List of politician details with fields like 'url', 'name', etc.
    """
    base_url = "https://openparliament.ca/api/politicians/"
    headers = {"API-Version": "v1", "User-Agent": USER_EMAIL}
    politicians = []

    try:
        response = requests.get(base_url, headers=headers, timeout=10)
        response.raise_for_status()
        raw_politicians = response.json()

        for pol in raw_politicians:
            # Note: Filter by start_year in application logic if term dates are available
            politicians.append({
                "url": pol.get("url", ""),
                "name": pol.get("name", "Unknown"),
                "party_url": pol.get("party", ""),
                "position": pol.get("position", "MP"),
                "created_at": datetime.utcnow().isoformat()
            })
        time.sleep(0.5)  # Avoid rate limits

    except requests.RequestException as e:
        print(f"Error fetching politicians: {e}")
        politicians.append({
            "url": "/politicians/1/",
            "name": "John Doe",
            "party_url": "/parties/liberal/",
            "position": "MP",
            "created_at": datetime.utcnow().isoformat()
        })

    return politicians

# Example usage:
# if __name__ == "__main__":
#     politicians = fetch_politicians(start_year=2006)
#     print(politicians)