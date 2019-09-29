from nba_api.stats.static.players import get_players, get_active_players, get_inactive_players


class Players:

    @staticmethod
    def all_players(self):
        return get_players()
