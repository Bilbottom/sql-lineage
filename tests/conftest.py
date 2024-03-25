"""
Shared fixtures for tests.
"""

import datetime
import textwrap

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
    return textwrap.dedent(
        """
        with
        aaa as (select 1 as aa),
        bbb as (select 2 as bb),
        ccc as (select 3 as cc, aa from aaa),
        ddd as (select 4 as dd, aa from aaa where aa not in (select bb from bbb))

        select *, $something
        from ccc
            inner join ddd using (aa)
        """
    )


@pytest.fixture(scope="session")
def mermaid_with_ctes() -> str:
    return textwrap.dedent(
        """\
        %% Generated at 2024-01-01 00:00:00
        flowchart TD
            aaa
            bbb
            ccc
            ddd
            final
            aaa --> ccc
            aaa --> ddd
            bbb --> ddd
            ccc --> final
            ddd --> final
        """
    )
