# tests/data_fetching/test_house_of_commons.py
"""
Unit tests for the house_of_commons module.
Ensures fetch_bills and fetch_votes return expected data and handle errors.
"""

from datetime import datetime
import pytest
from backend.api.data_fetching.house_of_commons import fetch_bills, fetch_votes


def test_fetch_bills_success(mock_requests):
    """
    Test fetching bills when the API request succeeds.
    """
    # Mock the API response
    url = "https://openparliament.ca/api/bills/"
    mock_data = [
        {
            "url": "/bills/42-1/C-10/",
            "number": "C-10",
            "name": "An Act to amend the Broadcasting Act",
            "summary": "This bill amends the Broadcasting Act.",
            "status": "passed",
            "sponsor": "/politicians/123/",
            "introduced_date": "2021-11-03"
        }
    ]
    mock_requests.get(url, json=mock_data, status_code=200)

    # Call the function
    result = fetch_bills(start_year=2006)

    # Assertions
    assert len(result) == 1
    assert result[0]["url"] == "/bills/42-1/C-10/"
    assert result[0]["number"] == "C-10"
    assert result[0]["title"] == "An Act to amend the Broadcasting Act"
    assert result[0]["description"] == "This bill amends the Broadcasting Act."
    assert result[0]["status"] == "passed"
    assert result[0]["introduced_by"] == "/politicians/123/"
    assert result[0]["introduced_date"] == "2021-11-03"
    assert "created_at" in result[0]
    assert datetime.fromisoformat(result[0]["created_at"])  # Verify ISO format


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
    assert result[0]["url"] == "/bills/1/"
    assert result[0]["number"] == "C-1"
    assert result[0]["title"] == "Sample Bill"
    assert result[0]["description"] == "A sample bill for testing"
    assert result[0]["status"] == "proposed"
    assert result[0]["introduced_by"] == "/politicians/1/"
    assert result[0]["introduced_date"] == "2006-01-01"
    assert "created_at" in result[0]


def test_fetch_votes_specific_bill_success(mock_requests):
    """
    Test fetching votes for a specific bill when the API request succeeds.
    """
    # Mock the API response
    bill_url = "/bills/42-1/C-10/"
    url = "https://openparliament.ca/api/votes/"
    mock_data = [
        {
            "url": "/votes/42-1/123/",
            "politician_url": "/politicians/123/",
            "bill_url": bill_url,
            "vote": "yes"
        }
    ]
    mock_requests.get(url, json=mock_data, status_code=200)

    # Call the function
    result = fetch_votes(bill_url=bill_url)

    # Assertions
    assert len(result) == 1
    assert result[0]["url"] == "/votes/42-1/123/"
    assert result[0]["politician_url"] == "/politicians/123/"
    assert result[0]["bill_url"] == bill_url
    assert result[0]["vote"] == "yes"
    assert "created_at" in result[0]
    assert datetime.fromisoformat(result[0]["created_at"])


def test_fetch_votes_all_success(mock_requests):
    """
    Test fetching all votes when no bill URL is provided.
    """
    # Mock the API response
    url = "https://openparliament.ca/api/votes/"
    mock_data = [
        {
            "url": "/votes/42-1/124/",
            "politician_url": "/politicians/124/",
            "bill_url": "/bills/42-1/C-11/",
            "vote": "no"
        }
    ]
    mock_requests.get(url, json=mock_data, status_code=200)

    # Call the function
    result = fetch_votes()

    # Assertions
    assert len(result) == 1
    assert result[0]["url"] == "/votes/42-1/124/"
    assert result[0]["politician_url"] == "/politicians/124/"
    assert result[0]["bill_url"] == "/bills/42-1/C-11/"
    assert result[0]["vote"] == "no"
    assert "created_at" in result[0]


def test_fetch_votes_request_error(mock_requests):
    """
    Test fetching votes when the API request fails.
    """
    # Mock a failed API request
    bill_url = "/bills/42-1/C-10/"
    url = "https://openparliament.ca/api/votes/"
    mock_requests.get(url, status_code=500)

    # Call the function
    result = fetch_votes(bill_url=bill_url)

    # Assertions
    assert len(result) == 1
    assert result[0]["url"] == "/votes/1/"
    assert result[0]["politician_url"] == "/politicians/1/"
    assert result[0]["bill_url"] == bill_url
    assert result[0]["vote"] == "yes"
    assert "created_at" in result[0]