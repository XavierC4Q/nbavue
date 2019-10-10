from nba_api.stats.static.teams import get_teams
from nba_api.stats.static.players import get_players, get_active_players, get_inactive_players
from flask import Blueprint, jsonify, make_response
from nba_api.stats.endpoints import commonteamroster
import requests
import datetime
import json

players_bp = Blueprint('players_bp', __name__, url_prefix='/players')


@players_bp.route('/roster/<team>', methods=['GET'])
def get_current_roster(team):
    season_start = datetime.datetime.now().year - 1
    season_end = datetime.datetime.now().year

    season_str = '{}-{}'.format(season_start, str(season_end)[2:])
    try:
        team_dict = commonteamroster.CommonTeamRoster(team_id=team, season=season_str).data_sets[0].get_dict()
        h = team_dict['headers']
        players = team_dict['data']
        roster = [dict(zip(h, player)) for player in players]

        return jsonify(roster)
    except:
        return make_response('Team {} not found'.format(team))



