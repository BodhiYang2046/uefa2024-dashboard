from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from scripts.scrape import scrape_uefa_data
from app.database import DatabaseManager

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def scrape_and_store():
    try:
        db_manager = DatabaseManager()
        db_manager.reset_database()
        data = scrape_uefa_data()
        db_manager.insert_data(data)
        print("Data scraped and stored successfully")
    except Exception as e:
        print(f"Error in scrape_and_store: {str(e)}")
        raise

with DAG('scrape_dag',
         default_args=default_args,
         description='A simple scrape DAG',
         schedule_interval=timedelta(days=1),
         catchup=False) as dag:

    scrape_task = PythonOperator(
        task_id='scrape_and_store',
        python_callable=scrape_and_store,
        dag=dag,
    )

    scrape_task