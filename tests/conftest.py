"""
Shared fixtures for tests.
"""

import datetime
import pathlib

import pytest

FIXTURES = pathlib.Path(__file__).parent / "fixtures"


def read_fixture(fixture_name: str) -> str:
    return pathlib.Path(FIXTURES / fixture_name).read_text(encoding="utf-8")


@pytest.fixture
def mock_datetime(monkeypatch):
    class MockDatetime(datetime.datetime):
        @classmethod
        def now(cls, **kwargs):
            return datetime.datetime(2024, 1, 1)

    monkeypatch.setattr(datetime, "datetime", MockDatetime)


@pytest.fixture(scope="session")
def sql_with_ctes() -> str:
    return read_fixture("mock.sql")


@pytest.fixture(scope="session")
def mermaid_with_ctes() -> str:
    return read_fixture("mock.mermaid")
