# tests/data_fetching/test_politicians.py
"""
Unit tests for the politicians module.
Ensures fetch_politicians returns expected data and handles errors.
"""

from datetime import datetime
import pytest
from backend.api.data_fetching.politicians import fetch_politicians


def test_fetch_politicians_success(mock_requests):
    """
    Test fetching politicians when the API request succeeds.
    """
    # Mock the API response
    url = "https://openparliament.ca/api/politicians/"
    mock_data = [
        {
            "url": "/politicians/123/",
            "name": "Jane Smith",
            "party": "/parties/liberal/",
            "position": "Minister"
        }
    ]
    mock_requests.get(url, json=mock_data, status_code=200)

    # Call the function
    result = fetch_politicians(start_year=2006)

    # Assertions
    assert len(result) == 1
    assert result[0]["url"] == "/politicians/123/"
    assert result[0]["name"] == "Jane Smith"
    assert result[0]["party_url"] == "/parties/liberal/"
    assert result[0]["position"] == "Minister"
    assert "created_at" in result[0]
    assert datetime.fromisoformat(result[0]["created_at"])


def test_fetch_politicians_request_error(mock_requests):
    """
    Test fetching politicians when the API request fails.
    """
    # Mock a failed API request
    url = "https://openparliament.ca/api/politicians/"
    mock_requests.get(url, status_code=500)

    # Call the function
    result = fetch_politicians(start_year=2006)

    # Assertions
    assert len(result) == 1
    assert result[0]["url"] == "/politicians/1/"
    assert result[0]["name"] == "John Doe"
    assert result[0]["party_url"] == "/parties/liberal/"
    assert result[0]["position"] == "MP"
    assert "created_at" in result[0]