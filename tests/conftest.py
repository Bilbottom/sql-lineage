"""
Shared fixtures for tests.
"""

import datetime
import pathlib

import pytest


@pytest.fixture
def mock_datetime(monkeypatch):
    class MockDatetime(datetime.datetime):
        @classmethod
        def now(cls, **kwargs):
            return datetime.datetime(2024, 1, 1)

    monkeypatch.setattr(datetime, "datetime", MockDatetime)


@pytest.fixture(scope="session")
def sql_with_ctes() -> str:
    return pathlib.Path("tests/fixtures/mock.sql").read_text(encoding="utf-8")


@pytest.fixture(scope="session")
def mermaid_with_ctes() -> str:
    return pathlib.Path("tests/fixtures/mock.mermaid").read_text(encoding="utf-8")
