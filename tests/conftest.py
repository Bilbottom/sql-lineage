"""
Shared fixtures for tests.
"""

import textwrap

import pytest


@pytest.fixture
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


@pytest.fixture
def mermaid_with_ctes() -> str:
    return textwrap.dedent(
        """\
        graph TD
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
