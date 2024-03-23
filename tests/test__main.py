"""
Unit tests for the ``sql_lineage.lineage`` module.
"""

import pathlib

import pytest

import sql_lineage.main as main


def test__main(tmp_path: pathlib.Path, sql_with_ctes: str, mermaid_with_ctes: str):
    """
    Test that the CLI opens and writes files correctly.
    """
    mermaid_path = tmp_path / "test.mermaid"
    sql_path = tmp_path / "test.sql"
    sql_path.write_text(sql_with_ctes, encoding="utf-8")

    main.main(file=str(sql_path))

    assert mermaid_path.exists()
    assert mermaid_path.read_text(encoding="utf-8") == mermaid_with_ctes


def test__main__file_not_found():
    """
    Test that the CLI raises a ``FileNotFoundError`` when the input file
    is not found.
    """
    with pytest.raises(FileNotFoundError):
        main.main(file="nonexistent.sql")


def test__main__value_error():
    """
    Test that the CLI raises a ``ValueError`` when the input file is not
    a file.
    """
    with pytest.raises(ValueError):
        main.main(file="tests")
