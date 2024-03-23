"""
CLI entry point for the ``sql_lineage`` package.
"""

import arguably

# This import is necessary for the CLI to work
import sql_lineage.main  # pylint: disable=unused-import

app = arguably.run  # sourcery skip: avoid-global-variables
if __name__ == "__main__":
    app()
