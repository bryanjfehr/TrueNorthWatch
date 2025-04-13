# tests/conftest.py
"""
Shared fixtures for PyTest.
Provides common setup for mocking HTTP requests across test modules.
"""

import pytest


@pytest.fixture
def mock_requests(requests_mock):
    """
    Fixture to provide a requests_mock instance for simulating HTTP requests.

    Args:
        requests_mock: PyTest fixture from the requests-mock library.

    Returns:
        requests_mock: Configured mock object for HTTP requests.
    """
    return requests_mock