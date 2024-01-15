from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

# Define default_args dictionary to specify the default parameters for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Instantiate a DAG
dag = DAG(
    'simple_bash_dag',
    default_args=default_args,
    description='A simple DAG with BashOperator',
    schedule_interval=timedelta(days=1),  # Set the schedule interval
)

# Task 1: Print "Hello"
task_hello = BashOperator(
    task_id='task_hello',
    bash_command='echo "Hello"',
    dag=dag,
)

# Task 2: Print "World"
task_world = BashOperator(
    task_id='task_world',
    bash_command='echo "World"',
    dag=dag,
)

# Set the task dependencies
task_hello >> task_world

if __name__ == "__main__":
    dag.cli()
