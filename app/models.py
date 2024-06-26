from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class TeamStanding(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    round = db.Column(db.String(50), nullable=False)
    week = db.Column(db.Float, nullable=False)
    day = db.Column(db.String(10), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.String(10), nullable=False)
    home_team = db.Column(db.String(50), nullable=False)
    home_xg = db.Column(db.Float, nullable=False)
    score = db.Column(db.String(10), nullable=False)
    away_xg = db.Column(db.Float, nullable=False)
    away_team = db.Column(db.String(50), nullable=False)
    attendance = db.Column(db.Integer, nullable=False)
    venue = db.Column(db.String(100), nullable=False)
    referee = db.Column(db.String(50), nullable=False)
    match_report = db.Column(db.String(100), nullable=False)
    notes = db.Column(db.String(255), nullable=True)
    scraped_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)