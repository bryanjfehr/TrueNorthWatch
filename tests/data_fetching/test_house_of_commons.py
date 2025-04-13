# tests/data_fetching/test_house_of_commons.py
"""
Unit tests for the house_of_commons module.
Ensures fetch_bills and fetch_votes return expected data and handle errors.
"""

from datetime import datetime
import pytest
from backend.data_fetching.house_of_commons import fetch_bills, fetch_votes


def test_fetch_bills_success(mock_requests):
    """
    Test fetching bills when the API request succeeds.
    """
    # Mock the API response
    url = "https://openparliament.ca/api/bills/"
    mock_data = [
        {
            "id": 1,
            "title": "Healthcare Act",
            "description": "Improves hospital funding",
            "status": "passed",
            "sponsor_id": 2
        }
    ]
    mock_requests.get(url, json=mock_data, status_code=200)

    # Call the function
    result = fetch_bills(start_year=2006)

    # Assertions
    assert len(result) == 1
    assert result[0]["id"] == 1
    assert result[0]["title"] == "Healthcare Act"
    assert result[0]["description"] == "Improves hospital funding"
    assert result[0]["status"] == "passed"
    assert result[0]["introduced_by"] == 2
    assert "created_at" in result[0]
    assert datetime.fromisoformat(result[0]["created_at"])


def test_fetch_bills_request_error(mock_requests):
    """
    Test fetching bills when the API request fails.
    """
    # Mock a failed API request
    url = "https://openparliament.ca/api/bills/"
    mock_requests.get(url, status_code=500)

    # Call the function
    result = fetch_bills(start_year=2006)

    # Assertions
    assert len(result) == 1
    assert result[0]["id"] == 1
    assert result[0]["title"] == "Sample Bill"
    assert result[0]["description"] == "A sample bill for testing"
    assert result[0]["status"] == "proposed"
    assert result[0]["introduced_by"] == 1
    assert "created_at" in result[0]


def test_fetch_votes_specific_bill_success(mock_requests):
    """
    Test fetching votes for a specific bill when the API request succeeds.
    """
    # Mock the API response
    bill_id = 1
    url = "https://openparliament.ca/api/votes/"
    mock_data = [
        {
            "id": 101,
            "politician_id": 3,
            "bill_id": bill_id,
            "vote": "yes"
        }
    ]
    mock_requests.get(url, json=mock_data, status_code=200)

    # Call the function
    result = fetch_votes(bill_id=bill_id)

    # Assertions
    assert len(result) == 1
    assert result[0]["id"] == 101
    assert result[0]["politician_id"] == 3
    assert result[0]["bill_id"] == bill_id
    assert result[0]["vote"] == "yes"
    assert "created_at" in result[0]
    assert datetime.fromisoformat(result[0]["created_at"])


def test_fetch_votes_all_success(mock_requests):
    """
    Test fetching all votes when no bill ID is provided.
    """
    # Mock the API response
    url = "https://openparliament.ca/api/votes/"
    mock_data = [
        {
            "id": 102,
            "politician_id": 4,
            "bill_id": 2,
            "vote": "no"
        }
    ]
    mock_requests.get(url, json=mock_data, status_code=200)

    # Call the function
    result = fetch_votes()

    # Assertions
    assert len(result) == 1
    assert result[0]["id"] == 102
    assert result[0]["politician_id"] == 4
    assert result[0]["bill_id"] == 2
    assert result[0]["vote"] == "no"
    assert "created_at" in result[0]


def test_fetch_votes_request_error(mock_requests):
    """
    Test fetching votes when the API request fails.
    """
    # Mock a failed API request
    bill_id = 1
    url = "https://openparliament.ca/api/votes/"
    mock_requests.get(url, status_code=500)

    # Call the function
    result = fetch_votes(bill_id=bill_id)

    # Assertions
    assert len(result) == 1
    assert result[0]["id"] == 1
    assert result[0]["politician_id"] == 1
    assert result[0]["bill_id"] == bill_id
    assert result[0]["vote"] == "yes"
    assert "created_at" in result[0]