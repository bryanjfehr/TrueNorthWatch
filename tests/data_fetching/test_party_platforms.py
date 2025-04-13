# tests/data_fetching/test_party_platforms.py
"""
Unit tests for the party_platforms module.
Ensures fetch_party_platform works for specific election years and handles errors.
"""

from datetime import datetime
import pytest
from backend.api.data_fetching.party_platforms import fetch_party_platform


def test_fetch_party_platform_success(mock_requests):
    """
    Test fetching a platform for a specific election year when the request succeeds.
    """
    # Mock the HTTP response
    party_name = "Liberal"
    election_year = 2006
    url = f"https://web.archive.org/web/2006*/https://liberal.ca/platform/2006"
    mock_html = """
    <html>
        <div class="platform-content">Support healthcare and jobs.</div>
    </html>
    """
    mock_requests.get(url, text=mock_html, status_code=200)

    # Call the function
    result = fetch_party_platform(party_name, election_year)

    # Assertions
    assert result["name"] == "Liberal"
    assert result["election_year"] == "2006"
    assert result["platform"] == "Support healthcare and jobs."
    assert "created_at" in result
    assert datetime.fromisoformat(result["created_at"])


def test_fetch_party_platform_no_content(mock_requests):
    """
    Test fetching a platform when no platform content is found.
    """
    # Mock the HTTP response with no platform content
    party_name = "NDP"
    election_year = 2010
    url = f"https://web.archive.org/web/2010*/https://ndp.ca/platform/2010"
    mock_html = "<html><div>No content here.</div></html>"
    mock_requests.get(url, text=mock_html, status_code=200)

    # Call the function
    result = fetch_party_platform(party_name, election_year)

    # Assertions
    assert result["name"] == "Ndp"
    assert result["election_year"] == "2010"
    assert result["platform"] == "No platform found"
    assert "created_at" in result


def test_fetch_party_platform_request_error(mock_requests):
    """
    Test fetching a platform when the HTTP request fails.
    """
    # Mock a failed HTTP request
    party_name = "Green"
    election_year = 2015
    url = f"https://web.archive.org/web/2015*/https://green.ca/platform/2015"
    mock_requests.get(url, status_code=500)

    # Call the function
    result = fetch_party_platform(party_name, election_year)

    # Assertions
    assert result["name"] == "Green"
    assert result["election_year"] == "2015"
    assert result["platform"] == "Error fetching platform"
    assert "created_at" in result