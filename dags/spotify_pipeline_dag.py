from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 3, 5),
    "retries": 1,
}

dag = DAG(
    "spotify_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False
)

def run_script(script_name):
    subprocess.run(["python", f"/opt/airflow/scripts/{script_name}"], check=True)

extract_task = PythonOperator(
    task_id="extract_data",
    python_callable=run_script,
    op_args=["extract.py"],
    dag=dag
)

transform_task = PythonOperator(
    task_id="transform_data",
    python_callable=run_script,
    op_args=["transform.py"],
    dag=dag
)

load_task = PythonOperator(
    task_id="load_data",
    python_callable=run_script,
    op_args=["load.py"],
    dag=dag
)

extract_task >> transform_task >> load_task
