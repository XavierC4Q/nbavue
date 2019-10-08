from nba_api.stats.static.teams import (
    get_teams,
    team_index_state,
    team_index_city,
    team_index_full_name,
)
from flask import Blueprint, jsonify

teams_bp = Blueprint('teams_bp', __name__, url_prefix='/teams')


@teams_bp.route('/all_teams', methods=['GET'])
def all_teams():
    return jsonify(get_teams())


@teams_bp.route('/state/<state>', methods=['GET'])
def team_state(state):
    return jsonify(team_index_state(state))
