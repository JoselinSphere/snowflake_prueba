"""
Tutorial_cloud
DAG auto-generated by Astro Cloud IDE.
"""

from airflow.decorators import dag
from astro import sql as aql
from astro.table import Table, Metadata
import pandas as pd
import pendulum


@aql.run_raw_sql(conn_id="snowflake_conn", task_id="sql_snowflake_conn", results_format="pandas_dataframe")
def sql_snowflake_conn_func():
    return """
    SELECT COUNT(*) FROM TABLA_PRUEBA;
    """

@aql.dataframe(task_id="python_1")
def python_1_func():
    print('Hola')

default_args={
    "owner": "joselin.rivas@sphere.com.pe,Open in Cloud IDE",
}

@dag(
    default_args=default_args,
    schedule="0 0 * * *",
    start_date=pendulum.from_format("2024-12-20", "YYYY-MM-DD").in_tz("UTC"),
    catchup=False,
    owner_links={
        "joselin.rivas@sphere.com.pe": "mailto:joselin.rivas@sphere.com.pe",
        "Open in Cloud IDE": "https://cloud.astronomer.io/cm4da6ei800x201jm5nqp75ko/cloud-ide/cm4wvy9kn0qf201m7nkardaxq/cm4x01jgx0sry01lcflf98zb3",
    },
)
def Tutorial_cloud():
    sql_snowflake_conn = sql_snowflake_conn_func()

    python_1 = python_1_func()

dag_obj = Tutorial_cloud()
