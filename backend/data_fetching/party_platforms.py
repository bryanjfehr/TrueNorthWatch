# backend/api/data_fetching/party_platforms.py
"""
Module for fetching political party platforms.
Supports fetching current and historical platforms from party websites or archives.
"""

import requests
from bs4 import BeautifulSoup
from typing import Dict, Optional
from datetime import datetime


def fetch_party_platform(party_name: str, year: Optional[int] = None) -> Dict[str, str]:
    """
    Fetch the platform for a given political party.

    Args:
        party_name (str): Name of the party (e.g., 'Liberal', 'Conservative').
        year (Optional[int]): Year for historical platform (e.g., 2006). If None,
            fetches the latest platform.

    Returns:
        Dict[str, str]: Dictionary containing platform details, including:
            - 'name': Party name
            - 'platform': Platform text
            - 'created_at': Timestamp of data retrieval

    Raises:
        requests.RequestException: If the request to the source fails.
    """
    # Normalize party name for URL construction
    party_name = party_name.lower().replace(" ", "-")
    base_url = f"https://{party_name}.ca/platform"  # Placeholder URL

    try:
        # If year is specified, try to fetch from an archive (e.g., Wayback Machine)
        if year:
            # Placeholder for archive URL
            archive_url = f"https://web.archive.org/web/{year}*/{base_url}"
            response = requests.get(archive_url, timeout=10)
        else:
            response = requests.get(base_url, timeout=10)

        response.raise_for_status()

        # Parse the page content
        soup = BeautifulSoup(response.text, "html.parser")
        # Placeholder: Extract platform text from a specific element
        platform_text = soup.find("div", class_="platform-content")
        platform = platform_text.get_text(strip=True) if platform_text else "No platform found"

        return {
            "name": party_name.capitalize(),
            "platform": platform,
            "created_at": datetime.utcnow().isoformat()
        }

    except requests.RequestException as e:
        # Log the error and return a default response
        print(f"Error fetching platform for {party_name}: {e}")
        return {
            "name": party_name.capitalize(),
            "platform": "Error fetching platform",
            "created_at": datetime.utcnow().isoformat()
        }


# Example usage:
# if __name__ == "__main__":
#     platform = fetch_party_platform("Liberal", year=2006)
#     print(platform)