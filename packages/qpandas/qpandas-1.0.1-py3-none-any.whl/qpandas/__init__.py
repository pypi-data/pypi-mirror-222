import os
from textwrap import dedent
from typing import Any

import pandas as pd

from qpandas.qpandas import _DIALECTS, PandaSQL, PandaSQLException, sqldf

_ROOT = os.path.abspath(os.path.dirname(__file__))


def _print_dialect_functions() -> None:
    for dialect in _DIALECTS:
        print(
            dedent(
                f"""\
            def {dialect}(query: str, env: dict[str, Any]) -> pd.DataFrame:
                return PandaSQL("{dialect}")(query, env)\n\n"""
            )
        )


def duckdb(query: str, env: dict[str, Any]) -> pd.DataFrame:
    return PandaSQL("duckdb")(query, env)


def postgres(query: str, env: dict[str, Any]) -> pd.DataFrame:
    return PandaSQL("postgres")(query, env)


def spark(query: str, env: dict[str, Any]) -> pd.DataFrame:
    return PandaSQL("spark")(query, env)


def trino(query: str, env: dict[str, Any]) -> pd.DataFrame:
    return PandaSQL("trino")(query, env)


def bigquery(query: str, env: dict[str, Any]) -> pd.DataFrame:
    return PandaSQL("bigquery")(query, env)


def hive(query: str, env: dict[str, Any]) -> pd.DataFrame:
    return PandaSQL("hive")(query, env)


def presto(query: str, env: dict[str, Any]) -> pd.DataFrame:
    return PandaSQL("presto")(query, env)


def sqlite(query: str, env: dict[str, Any]) -> pd.DataFrame:
    return PandaSQL("sqlite")(query, env)


def tsql(query: str, env: dict[str, Any]) -> pd.DataFrame:
    return PandaSQL("tsql")(query, env)


def clickhouse(query: str, env: dict[str, Any]) -> pd.DataFrame:
    return PandaSQL("clickhouse")(query, env)


def mysql(query: str, env: dict[str, Any]) -> pd.DataFrame:
    return PandaSQL("mysql")(query, env)


def redshift(query: str, env: dict[str, Any]) -> pd.DataFrame:
    return PandaSQL("redshift")(query, env)


def starrocks(query: str, env: dict[str, Any]) -> pd.DataFrame:
    return PandaSQL("starrocks")(query, env)


def dialect(query: str, env: dict[str, Any]) -> pd.DataFrame:
    return PandaSQL("dialect")(query, env)


def oracle(query: str, env: dict[str, Any]) -> pd.DataFrame:
    return PandaSQL("oracle")(query, env)


def snowflake(query: str, env: dict[str, Any]) -> pd.DataFrame:
    return PandaSQL("snowflake")(query, env)


def tableau(query: str, env: dict[str, Any]) -> pd.DataFrame:
    return PandaSQL("tableau")(query, env)


def _get_data(path):
    return os.path.join(_ROOT, "data", path)


def load_meat():
    filename = _get_data("meat.csv")
    df = pd.read_csv(filename, parse_dates=[0])
    return df


def load_births():
    filename = _get_data("births_by_month.csv")
    df = pd.read_csv(filename, parse_dates=[0])
    return df
