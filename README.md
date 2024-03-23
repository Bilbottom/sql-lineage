<div align="center">

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![tests](https://github.com/Bilbottom/sql-lineage/actions/workflows/tests.yaml/badge.svg)](https://github.com/Bilbottom/sql-lineage/actions/workflows/tests.yaml)
[![coverage](coverage.svg)](https://github.com/dbrgn/coverage-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/Bilbottom/sql-lineage)

[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)
[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Bilbottom/sql-lineage/main.svg)](https://results.pre-commit.ci/latest/github/Bilbottom/sql-lineage/main)
[![Sourcery](https://img.shields.io/badge/Sourcery-enabled-brightgreen)](https://sourcery.ai)

</div>

---

# SQL Lineage 🔀

Personal SQL lineage generator.

Built on the following awesome libraries:

- [SQLGlot](https://github.com/tobymao/sqlglot) for SQL parsing
- [arguably](https://github.com/treykeown/arguably) for the CLI

## So... what is this? 🤔

> [!NOTE]
>
> This project is still in development and currently only parses the CTEs of an SQL query since that's all I need for now.

I write _a lot_ of SQL, and I often need to understand "lineage" in lots of different ways.

Things like [dbt](https://www.getdbt.com/) and [SQLMesh](https://sqlmesh.com/) are great for object lineage (tables, columns, etc.), but I often need to understand "lineage" like the CTE lineage in a query, among other things.

This project is just a personal tool to help me generate lineage diagrams (in [Mermaid](https://mermaid.js.org/) syntax) for SQL queries to fit that requirement.

Upcoming improvements will (hopefully) include:

- Column lineage to Mermaid
- Semantic edges (e.g. distinguish between `JOIN`, `WHERE`, `UNION`, etc.)
- Lineage for multiple files in a single diagram

## Installation ⬇️

Grab a copy from PyPI like usual (note the `bills-` prefix):

```
pip install bills-sql-lineage
```

## Usage 📖

Pass the path to a SQL file to the `lineage` command to generate the lineage as a [Mermaid](https://mermaid.js.org/) diagram:

```
lineage path/to/file.sql
```

This will write a Mermaid diagram to `path/to/file.mermaid`. You can control the target with the second argument:

```
lineage path/to/file.sql path/to/output.mermaid
```
