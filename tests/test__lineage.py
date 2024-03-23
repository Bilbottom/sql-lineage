"""
Unit tests for the ``sql_lineage.lineage`` module.
"""

import textwrap

import pytest

import sql_lineage.lineage as lineage


@pytest.fixture
def sql_with_ctes() -> str:
    return textwrap.dedent(
        """
        with
            aaa as (select 1 as aa),
            bbb as (select 2 as bb),
            ccc as (select 3 as cc, aa from aaa),
            ddd as (select 4 as dd, aa from aaa where aa not in (select bb from bbb))

        select *
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


def test__parse_ctes_to_mermaid(sql_with_ctes: str, mermaid_with_ctes: str):
    """
    Test the ``parse_ctes`` function.
    """
    assert lineage.sql_to_mermaid(sql_with_ctes) == mermaid_with_ctes
