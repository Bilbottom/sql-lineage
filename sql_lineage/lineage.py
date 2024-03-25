"""
Parsers for SQL queries and Mermaid graphs.
"""

from __future__ import annotations

import contextlib

import sqlglot
from sqlglot import exp
from sqlglot.optimizer import qualify

Nodes = list[str]
Edges = list[tuple[str, str]]  # Directed edges, source --> target.


def _parse_ctes(sql: str) -> [Nodes, Edges]:
    """
    Parse an SQL query into nodes and edges based on CTEs.
    """
    nodes, edges = [], []
    parsed = sqlglot.parse_one(sql)
    with contextlib.suppress(Exception):
        # There isn't a hard requirement for the query to be valid SQL,
        # but it's better if it is
        parsed = qualify.qualify(parsed)

    # Lazy and error-prone CTE sourcing
    for cte in parsed.find_all(exp.CTE):
        nodes.append(cte.alias)
        edges.extend((tbl.name, cte.alias) for tbl in cte.find_all(exp.Table))

    parsed.args["with"] = None  # Dirty hack to remove the CTEs from the query
    nodes.append("final")
    edges.extend((tbl.name, "final") for tbl in parsed.find_all(exp.Table))

    return nodes, edges


def _to_mermaid(nodes: Nodes, edges: Edges) -> str:
    """
    Convert nodes and edges into a Mermaid graph.
    """
    mermaid = "graph TD\n"

    for node in nodes:
        mermaid += f"    {node}\n"  # pylint: disable=consider-using-join

    for edge in edges:
        mermaid += f"    {edge[0]} --> {edge[1]}\n"

    return mermaid


def sql_to_mermaid(sql: str) -> str:
    """
    Convert an SQL query into a Mermaid graph.
    """
    nodes, edges = _parse_ctes(sql)

    return _to_mermaid(nodes, edges)
