"""
An SQL lineage tool, built on the awesome SQLGlot library.
"""

from __future__ import annotations

import pathlib

import arguably

from sql_lineage import lineage


def _to_path(file_path: str, validate: bool = False) -> pathlib.Path:
    """
    Convert a file path to a pathlib.Path object.
    """
    path = pathlib.Path(file_path)
    if validate:
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        if not path.is_file():
            raise ValueError(f"Not a file: {file_path}")

    return path


@arguably.command
def main(file: str, target: str = None) -> None:
    """
    Parse an SQL file into a Mermaid graph by tracing CTEs.
    """
    file_path = _to_path(file, validate=True)
    target_path = _to_path(target) if target else file_path.with_suffix(".mermaid")

    sql = file_path.read_text(encoding="utf-8")
    mermaid = lineage.sql_to_mermaid(sql)

    target_path.write_text(mermaid, encoding="utf-8")
    # Switch to logging at some point
    print(f"Mermaid graph written to: {target_path.absolute()}")
