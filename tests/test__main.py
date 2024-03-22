"""
Unit tests for the ``sql_lineage.main`` module.
"""

import sql_lineage.main as main


def test__main(monkeypatch):
    """
    Test the ``main`` function.
    """
    main.main()
