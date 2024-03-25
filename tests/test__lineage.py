"""
Unit tests for the ``sql_lineage.lineage`` module.
"""

from sql_lineage import lineage


def test__parse_ctes_to_mermaid(
    mock_datetime,
    sql_with_ctes: str,
    mermaid_with_ctes: str,
):
    """
    Test that SQL queries with CTEs are parsed into Mermaid graphs.
    """
    assert lineage.sql_to_mermaid(sql_with_ctes) == mermaid_with_ctes
