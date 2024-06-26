# from flask import Blueprint, render_template, jsonify
# from app.models import TeamStanding

# main = Blueprint('main', __name__)

# @main.route('/')
# def index():
#     return render_template('index.html')

# @main.route('/api/team_stats')
# def team_stats():
#     teams = Team.query.all()
#     stats = [{'name': team.name, 'points': team.points} for team in teams]
#     return jsonify(stats)

# @main.route('/api/recent_matches')
# def recent_matches():
#     matches = Match.query.order_by(Match.date.desc()).limit(5).all()
#     results = [{'home': match.home_team, 'away': match.away_team, 'score': f"{match.home_score}-{match.away_score}"} for match in matches]
#     return jsonify(results)


from flask import Blueprint, render_template, jsonify, request, redirect, url_for, flash
from app.models import db, TeamStanding

main = Blueprint('main', __name__)

@main.route('/')
def index():
    standings = TeamStanding.query.all()
    return render_template('index.html', standings=standings)

@main.route('/add', methods=['GET', 'POST'])
def add_standing():
    if request.method == 'POST':
        round = request.form['round']
        week = request.form['week']
        day = request.form['day']
        date = request.form['date']
        time = request.form['time']
        home_team = request.form['home_team']
        home_xg = request.form['home_xg']
        score = request.form['score']
        away_xg = request.form['away_xg']
        away_team = request.form['away_team']
        attendance = request.form['attendance']
        venue = request.form['venue']
        referee = request.form['referee']
        match_report = request.form['match_report']
        notes = request.form.get('notes')

        new_standing = TeamStanding(
            round=round,
            week=week,
            day=day,
            date=date,
            time=time,
            home_team=home_team,
            home_xg=home_xg,
            score=score,
            away_xg=away_xg,
            away_team=away_team,
            attendance=attendance,
            venue=venue,
            referee=referee,
            match_report=match_report,
            notes=notes
        )

        try:
            db.session.add(new_standing)
            db.session.commit()
            flash('New standing added successfully!', 'success')
            return redirect(url_for('main.index'))
        except Exception as e:
            flash('Error adding standing: ' + str(e), 'danger')

    return render_template('add_standing.html')

@main.route('/update/<int:id>', methods=['GET', 'POST'])
def update_standing(id):
    standing = TeamStanding.query.get_or_404(id)

    if request.method == 'POST':
        standing.round = request.form['round']
        standing.week = request.form['week']
        standing.day = request.form['day']
        standing.date = request.form['date']
        standing.time = request.form['time']
        standing.home_team = request.form['home_team']
        standing.home_xg = request.form['home_xg']
        standing.score = request.form['score']
        standing.away_xg = request.form['away_xg']
        standing.away_team = request.form['away_team']
        standing.attendance = request.form['attendance']
        standing.venue = request.form['venue']
        standing.referee = request.form['referee']
        standing.match_report = request.form['match_report']
        standing.notes = request.form.get('notes')

        try:
            db.session.commit()
            flash('Standing updated successfully!', 'success')
            return redirect(url_for('main.index'))
        except Exception as e:
            flash('Error updating standing: ' + str(e), 'danger')

    return render_template('update_standing.html', standing=standing)

@main.route('/delete/<int:id>', methods=['POST'])
def delete_standing(id):
    standing = TeamStanding.query.get_or_404(id)

    try:
        db.session.delete(standing)
        db.session.commit()
        flash('Standing deleted successfully!', 'success')
        return redirect(url_for('main.index'))
    except Exception as e:
        flash('Error deleting standing: ' + str(e), 'danger')
        return redirect(url_for('main.index'))