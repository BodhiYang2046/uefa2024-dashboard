from flask import Flask
from flask_migrate import Migrate
from app.models import db
from dotenv import load_dotenv
import os

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
    # from app import routes
    # app.register_blueprint(routes.bq)

    with app.app_context():
        # Import routes here to avoid circular import issues
        from app.routes import main as main_blueprint
        app.register_blueprint(main_blueprint)
        db.create_all()

    return app