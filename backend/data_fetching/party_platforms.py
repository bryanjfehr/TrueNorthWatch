# backend/api/data_fetching/party_platforms.py
"""
Module for fetching political party platforms via web scraping for specific election years.
Note: Open Parliament API does not provide party platforms; consider Poltext or party archives.
"""

import requests
from bs4 import BeautifulSoup
from typing import Dict
from datetime import datetime

def fetch_party_platform(party_name: str, election_year: int) -> Dict[str, str]:
    """
    Fetch the platform for a given political party and election year.

    Args:
        party_name (str): Name of the party (e.g., 'Liberal', 'Conservative').
        election_year (int): Year of the election campaign (e.g., 2006).

    Returns:
        Dict[str, str]: Dictionary with 'name', 'election_year', 'platform', and 'created_at'.
    """
    party_name = party_name.lower().replace(" ", "-")
    # Placeholder URL; update with actual party platform URLs or use Poltext/archives
    base_url = f"https://{party_name}.ca/platform/{election_year}"

    try:
        # Use Wayback Machine for historical data if direct URL unavailable
        archive_url = f"https://web.archive.org/web/{election_year}*/{base_url}"
        response = requests.get(archive_url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        platform_text = soup.find("div", class_="platform-content")
        platform = platform_text.get_text(strip=True) if platform_text else "No platform found"

        return {
            "name": party_name.capitalize(),
            "election_year": str(election_year),
            "platform": platform,
            "created_at": datetime.utcnow().isoformat()
        }

    except requests.RequestException as e:
        print(f"Error fetching platform for {party_name} in {election_year}: {e}")
        return {
            "name": party_name.capitalize(),
            "election_year": str(election_year),
            "platform": "Error fetching platform",
            "created_at": datetime.utcnow().isoformat()
        }

# Example usage:
# if __name__ == "__main__":
#     platform = fetch_party_platform("Liberal", 2006)
#     print(platform)