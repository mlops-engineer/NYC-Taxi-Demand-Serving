import os
from datetime import datetime, timedelta
from airflow import models
from airflow.operators.bash_operator import BashOperator

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), './'))

default_args = {
    'owner': 'default',
    'depends_on_past': False,
    'start_date': datetime(2021, 5, 16),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
    'project_id': 'your_project'
}

bash_command = f"""
    python3 {root_path}/main.py --dev_env prod
"""

with models.DAG(
        dag_id='Train-nyc_taxi_demand_every_week',
        description='Train NYC taxi demand',
        schedule_interval='1 15 * * 0',
        default_args=default_args) as dag:

    train_operator = BashOperator(
        dag=dag,
        task_id='train',
        bash_command=bash_command
    )

    train_operator
