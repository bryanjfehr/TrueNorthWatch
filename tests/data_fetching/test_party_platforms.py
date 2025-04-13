# tests/data_fetching/test_party_platforms.py
"""
Unit tests for the party_platforms module.
Ensures the fetch_party_platform function works for both current and historical data,
and handles errors gracefully.
"""

from datetime import datetime
import pytest
from backend.data_fetching.party_platforms import fetch_party_platform


def test_fetch_party_platform_current_success(mock_requests):
    """
    Test fetching the current platform for a party when the request succeeds.
    """
    # Mock the HTTP response
    party_name = "Liberal"
    url = f"https://liberal.ca/platform"
    mock_html = """
    <html>
        <div class="platform-content">Support healthcare and jobs.</div>
    </html>
    """
    mock_requests.get(url, text=mock_html, status_code=200)

    # Call the function
    result = fetch_party_platform(party_name)

    # Assertions
    assert result["name"] == "Liberal"
    assert result["platform"] == "Support healthcare and jobs."
    assert "created_at" in result
    assert datetime.fromisoformat(result["created_at"])  # Ensure valid datetime


def test_fetch_party_platform_historical_success(mock_requests):
    """
    Test fetching a historical platform for a party when the request succeeds.
    """
    # Mock the HTTP response
    party_name = "Conservative"
    year = 2006
    url = f"https://web.archive.org/web/{year}*/https://conservative.ca/platform"
    mock_html = """
    <html>
        <div class="platform-content">Reduce taxes for families.</div>
    </html>
    """
    mock_requests.get(url, text=mock_html, status_code=200)

    # Call the function
    result = fetch_party_platform(party_name, year=year)

    # Assertions
    assert result["name"] == "Conservative"
    assert result["platform"] == "Reduce taxes for families."
    assert "created_at" in result
    assert datetime.fromisoformat(result["created_at"])


def test_fetch_party_platform_no_content(mock_requests):
    """
    Test fetching a platform when no platform content is found on the page.
    """
    # Mock the HTTP response with empty content
    party_name = "NDP"
    url = f"https://ndp.ca/platform"
    mock_html = "<html><div>No content here.</div></html>"
    mock_requests.get(url, text=mock_html, status_code=200)

    # Call the function
    result = fetch_party_platform(party_name)

    # Assertions
    assert result["name"] == "Ndp"  # Note: Capitalization based on input
    assert result["platform"] == "No platform found"
    assert "created_at" in result


def test_fetch_party_platform_request_error(mock_requests):
    """
    Test fetching a platform when the HTTP request fails.
    """
    # Mock a failed HTTP request
    party_name = "Green"
    url = f"https://green.ca/platform"
    mock_requests.get(url, status_code=500)

    # Call the function
    result = fetch_party_platform(party_name)

    # Assertions
    assert result["name"] == "Green"
    assert result["platform"] == "Error fetching platform"
    assert "created_at" in result