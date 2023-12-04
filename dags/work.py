from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.decorators import task
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'email': ['cosheckablack451@mail.ru'],
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'email_on_retry': False,
    'depends_on_past': False,
    'email_on_failure': False,
    'priority_weight': 10,
    'execution_timeout': timedelta(hours=10),
    'dag_run_timeout': timedelta(hours=10)
}

with DAG(
        dag_id='first_dag',
        schedule_interval='0 16 * * *',
        start_date=datetime(2022, 1, 1),
        catchup=False,
        description=f"""Описание DAG, которое будет видно в airflow""",
        tags=['firs_dag'],
        default_args=default_args
) as dag:
    task1 = BashOperator(
    task_id='task1',
    bash_command='echo "This is task 1"')

    task2 = BashOperator(
        task_id='task2',
        bash_command='echo "This is task 2"')

    task3 = BashOperator(
        task_id='task3',
        bash_command='echo "This is task 3"')

    task1 >> task2 >> task3