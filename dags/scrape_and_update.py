from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.google.cloud.transfers.postgres_to_gcs import PostgresToGCSOperator
from datetime import datetime, timedelta
from app.scrape import scrape_uefa_data
from app import db, create_app
from app.models import TeamStanding

from scripts.scrape import scrape_uefa_data
from app.database import DatabaseManager

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 6, 25),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'scrape_and_update',
    default_args=default_args,
    description='A DAG to scrape UEFA data and update PostgreSQL',
    schedule_interval=timedelta(days=1),
)

# def scrape_and_update(**kwargs):
#     app = create_app()
#     init_db(app)
#     with app.app_context():
#         df = scrape_uefa_data()
#         if df is not None:
#             for _, row in df.iterrows():
#                 standing = TeamStanding(
#                     round=row['Round'],
#                     week=row['Wk'],
#                     day=row['Day'],
#                     date=datetime.strptime(row['Date'], '%Y-%m-%d'),
#                     time=row['Time'],
#                     home_team=row['Home'],
#                     home_xg=float(row['xG']),
#                     score=row['Score'],
#                     away_xg=float(row['xG.1']),
#                     away_team=row['Away'],
#                     attendance=int(row['Attendance'].replace(',', '')),
#                     venue=row['Venue'],
#                     referee=row['Referee'],
#                     match_report=row['Match Report'],
#                     notes=row['Notes'] if 'Notes' in row else None,
#                     scraped_at=datetime.now()
#                 )
#                 db.session.add(standing)
#             db.session.commit()

# scrape_and_update_task = PythonOperator(
#     task_id='scrape_and_update',
#     python_callable=scrape_and_update,
#     dag=dag,
# )

def scrape_and_store():
    db_manager = DatabaseManager()
    db_manager.reset_database()
    data = scrape_uefa_data()
    db_manager.insert_data(data)

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