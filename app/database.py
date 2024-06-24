from app import db
from app.models import Team, Match

def init_db():
    db.create_all()

def populate_sample_data():
    # Add sample teams
    teams = [
        Team(name='Real Madrid', points=82),
        Team(name='Barcelona', points=78),
        Team(name='Atletico Madrid', points=71),
    ]
    db.session.add_all(teams)

    # Add sample matches
    matches = [
        Match(date='2023-05-01', home_team='Real Madrid', away_team='Barcelona', home_score=2, away_score=1),
        Match(date='2023-05-05', home_team='Atletico Madrid', away_team='Real Madrid', home_score=0, away_score=2),
    ]
    db.session.add_all(matches)

    db.session.commit()