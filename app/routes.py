from flask import Blueprint, render_template, jsonify
from app.models import Team, Match

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/api/team_stats')
def team_stats():
    teams = Team.query.all()
    stats = [{'name': team.name, 'points': team.points} for team in teams]
    return jsonify(stats)

@main.route('/api/recent_matches')
def recent_matches():
    matches = Match.query.order_by(Match.date.desc()).limit(5).all()
    results = [{'home': match.home_team, 'away': match.away_team, 'score': f"{match.home_score}-{match.away_score}"} for match in matches]
    return jsonify(results)