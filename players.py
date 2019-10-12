from nba_api.stats.static.teams import get_teams
from nba_api.stats.static.players import get_players, get_active_players, get_inactive_players
from flask import Blueprint, jsonify, make_response
from nba_api.stats.endpoints import commonteamroster, playerprofilev2
import requests
import datetime

players_bp = Blueprint('players_bp', __name__, url_prefix='/players')


@players_bp.route('/roster/<team>', methods=['GET'])
def get_current_roster(team):
    season_start = datetime.datetime.now().year - 1
    season_end = datetime.datetime.now().year

    season_str = '{}-{}'.format(season_start, str(season_end)[2:])
    try:
        team_dict = commonteamroster.CommonTeamRoster(team_id=team, season=season_str).common_team_roster.get_dict()
        h = team_dict['headers']
        players = team_dict['data']
        roster = [dict(zip(h, player)) for player in players]

        return jsonify(roster)
    except:
        return make_response('Team {} not found'.format(team))


@players_bp.route('/player/basic_info/<playerId>/<perMode>')
def basic_player_info(playerId, perMode):
    try:
        player_dict = playerprofilev2.PlayerProfileV2(player_id=playerId, per_mode36=perMode).career_totals_regular_season.get_dict()
        return jsonify(player_dict)
    except:
        return make_response('Player {} not found'.format(playerId))

