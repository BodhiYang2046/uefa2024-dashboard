from app import db
from datetime import datetime

class TeamStandings(db.Model):
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

    def to_dict(self):
        return {
            "id": self.id,
            "round": self.round,
            "week": self.week,
            "day": self.day,
            "date": self.date.strftime('%Y-%m-%d') if self.date else None,
            "time": self.time if isinstance(self.time, str) else self.time.strftime('%H:%M') if self.time else None,
            "home_team": self.home_team,
            "home_xg": self.home_xg,
            "score": self.score,
            "away_xg": self.away_xg,
            "away_team": self.away_team,
            "attendance": self.attendance,
            "venue": self.venue,
            "referee": self.referee,
            "match_report": self.match_report,
            "notes": self.notes
        }