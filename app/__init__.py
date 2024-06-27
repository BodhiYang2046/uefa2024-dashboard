from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()  # This loads the variables from .env

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Load configuration from environment variables or a config file
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints
    with app.app_context():
        # Import routes here to avoid circular import issues
        from app.routes import main as main_blueprint
        app.register_blueprint(main_blueprint)
        db.create_all()

    return app