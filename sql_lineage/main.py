"""
An SQL lineage tool, built on the awesome SQLGlot library.
"""

import sqlglot
from sqlglot import exp
from sqlglot.optimizer import qualify

Nodes = list[str]
Edges = list[tuple[str, str]]  # Directed edges, source --> target.


def parse_ctes(sql: str) -> [Nodes, Edges]:
    """
    Parse an SQL query into nodes and edges based on CTEs.
    """
    parsed = qualify.qualify(sqlglot.parse_one(sql))
    nodes, edges = [], []

    # Lazy and error-prone CTE sourcing
    for cte in parsed.find_all(exp.CTE):
        nodes.append(cte.alias)
        edges.extend((tbl.name, cte.alias) for tbl in cte.find_all(exp.Table))

    parsed.args["with"] = None  # Dirty hack to remove the CTEs from the query
    nodes.append("final")
    edges.extend((tbl.name, "final") for tbl in parsed.find_all(exp.Table))

    return nodes, edges


def to_mermaid(nodes: Nodes, edges: Edges) -> str:
    """
    Convert nodes and edges into a Mermaid graph.
    """
    mermaid = "graph TD\n"

    for node in nodes:
        mermaid += f"    {node}\n"  # pylint: disable=consider-using-join

    for edge in edges:
        mermaid += f"    {edge[0]} --> {edge[1]}\n"

    return mermaid


def main() -> None:
    """
    Entry point into the SQL lineage tool.
    """


if __name__ == "__main__":
    main()  # pragma: no cover
