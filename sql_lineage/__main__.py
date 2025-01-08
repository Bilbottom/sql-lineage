"""
CLI entry point for the ``sql_lineage`` package.
"""

import arguably

# This import is necessary for the CLI to work
import sql_lineage.main  # noqa

app = arguably.run
if __name__ == "__main__":
    app()
