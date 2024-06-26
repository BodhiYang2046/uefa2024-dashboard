from app import db
from app.models import Team, Match


def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()