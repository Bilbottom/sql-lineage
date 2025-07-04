<div align="center">

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![tests](https://github.com/billwallis/bills-sql-lineage/actions/workflows/tests.yaml/badge.svg)](https://github.com/billwallis/bills-sql-lineage/actions/workflows/tests.yaml)
[![coverage](coverage.svg)](https://github.com/dbrgn/coverage-badge)
[![GitHub last commit](https://img.shields.io/github/last-commit/billwallis/bills-sql-lineage)](https://shields.io/badges/git-hub-last-commit)

[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/billwallis/bills-sql-lineage/main.svg)](https://results.pre-commit.ci/latest/github/billwallis/bills-sql-lineage/main)

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

- Semantic edges (e.g. distinguish between `JOIN`, `WHERE`, `UNION`, etc.)
- Support for parameterised queries (e.g. with Jinja blocks, like [dbt](https://www.getdbt.com/))
- Parsing only the `SELECT` part of a SQL file that includes DDL/DML commands
- Lineage for multiple files in a single diagram
- Column lineage to Mermaid

## Installation ⬇️

Grab a copy from PyPI like usual:

```
pip install bills-sql-lineage
```

## Usage 📖

> [!WARNING]
>
> This is likely to change significantly as the project evolves.

Pass the path to a SQL file to the `lineage` command to generate the lineage as a [Mermaid](https://mermaid.js.org/) diagram:

```
lineage path/to/file.sql
```

This will write a Mermaid diagram to `path/to/file.mermaid`. You can control the target path with the `--target` argument:

```
lineage path/to/file.sql --target path/to/output.mermaid
```

By default, the SQL dialect will be inferred by SQLGlot, but you can specify a dialect with the `--dialect` argument:

```
lineage path/to/file.sql --dialect snowflake
```

## Example 📝

Given the following SQL query:

```sql
with

aaa as (select 1 as aa),
bbb as (select 2 as bb),
ccc as (select 3 as cc, aa from aaa),
ddd as (select 4 as dd, aa from aaa where aa not in (select bb from bbb))

select *
from ccc
    inner join ddd using (aa)
```

...the following Mermaid diagram will be generated:

```mermaid
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
```

Note that the `final` node is an alias for the final `SELECT` statement since the final `SELECT` statement is not a CTE.
