from airflow import DAG
from airflow.providers.google.cloud.transfers.postgres_to_gcs import PostgresToGCSOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'export_to_gcs',
    default_args=default_args,
    description='A DAG to export data from PostgreSQL to GCS',
    schedule_interval=timedelta(days=1),
)

export_to_gcs_task = PostgresToGCSOperator(
    task_id='export_to_gcs',
    postgres_conn_id='postgres_default',
    google_cloud_storage_conn_id='google_cloud_default',
    sql='SELECT * FROM team_standing',
    bucket='your-gcs-bucket',
    filename='uefa_data/{{ ds }}/standings.csv',
    export_format='csv',
    dag=dag,
)