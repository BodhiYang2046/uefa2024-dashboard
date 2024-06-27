from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
import pandas as pd
from app.models import db, TeamStandings
from scripts.scrape import scrape_uefa_data
from config import Config
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DatabaseManager:
    def __init__(self):
        self.config = Config()
        self.engine = create_engine(self.config.SQLALCHEMY_DATABASE_URI)
        # self.Session = sessionmaker(bind=self.engine)

    # # def init_db(self, app):
    #     db.init_app(app)
    #     with app.app_context():
    #         db.create_all()

    # def get_session(self):
    #     return self.Session()

    def reset_database(self):
        logger.info("Resetting database...")
        meta = MetaData(bind=self.engine)
        meta.reflect()

        table_name = 'team_standings'
        if table_name in meta.tables:
            table = Table(table_name, meta)
            table.drop()
        
        TeamStandings.__table__.create(bind=self.engine)
        logger.info("Database reset complete")

    def insert_data(self, data):
        if data.empty:
            logger.warning("No data to insert")
            return

        logger.info(f"Inserting {len(data)} rows into database")
        try:
            data.to_sql('team_standings', self.engine, if_exists='append', index=False)
            logger.info(f"Inserted {len(data)} rows into database")
        except Exception as e:
            logger.error(f"Error inserting data: {e}")
            raise

if __name__ == "__main__":
    db_manager = DatabaseManager()
    db_manager.reset_database()
    data = scrape_uefa_data()
    db_manager.insert_data(data)