"""
Unit tests for the ``sql_lineage.main`` module.
"""

import textwrap

import pytest

import sql_lineage.main as main


@pytest.fixture
def nodes() -> main.Nodes:
    return ["aaa", "bbb", "ccc", "ddd", "final"]


@pytest.fixture
def edges() -> main.Edges:
    return [
        ("aaa", "ccc"),
        ("aaa", "ddd"),
        ("bbb", "ddd"),
        ("ccc", "final"),
        ("ddd", "final"),
    ]


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


def test__parse_ctes(nodes: main.Nodes, edges: main.Edges, sql_with_ctes: str):
    """
    Test the ``parse_ctes`` function.
    """
    assert main.parse_ctes(sql_with_ctes) == (nodes, edges)


def test__to_mermaid(nodes: main.Nodes, edges: main.Edges, mermaid_with_ctes: str):
    """
    Test the ``to_mermaid`` function.
    """
    assert main.to_mermaid(nodes, edges) == mermaid_with_ctes
