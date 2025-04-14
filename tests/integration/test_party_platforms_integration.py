# tests/integration/test_party_platforms_integration.py
"""
Integration tests for the party_platforms module.
These tests use real URLs to fetch actual platform data.
"""

import pytest
from backend.api.data_fetching.party_platforms import fetch_party_platform

@pytest.mark.integration
def test_fetch_party_platform_real():
    """
    Test fetching real platform data for a specific party and election year.
    """
    party_name = "Liberal"
    election_year = 2006
    platform_data = fetch_party_platform(party_name, election_year)

    # Assertions to verify data is fetched and formatted
    assert isinstance(platform_data, dict), "Platform data should be a dictionary"
    assert platform_data["name"] == "Liberal", "Party name should match"
    assert platform_data["election_year"] == "2006", "Election year should match"
    assert "platform" in platform_data, "Platform text should be present"
    assert isinstance(platform_data["platform"], str), "Platform should be a string"
    assert len(platform_data["platform"]) > 0, "Platform text should not be empty"
    assert "created_at" in platform_data, "Created_at timestamp should be present"