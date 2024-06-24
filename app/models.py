from app import db

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    points = db.Column(db.Integer, default=0)

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    home_team = db.Column(db.String(64), nullable=False)
    away_team = db.Column(db.String(64), nullable=False)
    home_score = db.Column(db.Integer, nullable=False)
    away_score = db.Column(db.Integer, nullable=False)