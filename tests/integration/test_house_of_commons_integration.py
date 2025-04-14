# tests/integration/test_house_of_commons_integration.py
"""
Integration tests for the house_of_commons module.
These tests use real URLs to fetch actual data from the Open Parliament API.
"""

import pytest
from backend.api.data_fetching.house_of_commons import fetch_bills

@pytest.mark.integration
def test_fetch_bills_real():
    """
    Test fetching real bills from the Open Parliament API and verify formatting.
    """
    # Call the function with a real URL (no mocking)
    bills = fetch_bills(start_year=2006)

    # Assertions to check if data is fetched and formatted correctly
    assert isinstance(bills, list), "Bills should be returned as a list"
    assert len(bills) > 0, "At least one bill should be fetched"
    assert "url" in bills[0], "Each bill should have a URL"
    assert "number" in bills[0], "Each bill should have a number"
    assert "title" in bills[0], "Each bill should have a title"
    assert "description" in bills[0], "Each bill should have a description"
    assert "status" in bills[0], "Each bill should have a status"
    assert "introduced_by" in bills[0], "Each bill should have an introducer"
    assert "introduced_date" in bills[0], "Each bill should have an introduced date"
    assert "created_at" in bills[0], "Each bill should have a created_at timestamp"