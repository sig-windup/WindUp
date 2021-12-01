from logic.solve_WAR import Hitter
from predict.models import Hitter_stats

def get_players(lineup_objects):
    players = []
    for lo in lineup_objects:
        players.append(lo.name)
    return players

def make_hitter_objects(hitter_names, team, opposite_team):
    hitter_object_array = []
    for hn in hitter_names:
        x = Hitter_stats.objects.get(name=hn, team= team, opposite_team = opposite_team)
        h = Hitter(x.name, x.team, x.opposite_team, x.game, x.pa, x.ab, x.h, x.oneb, x.twob, x.threeb, x.hr, x.r, x.bb,
                   x.ibb, x.hbp, x.k, x.sf, x.sh, x.gidp, x.sb, x.cs, x.avg)
        hitter_object_array.append(h)
    return hitter_object_array

def pitcher_WAR(pitcher_stat_object):
    return pitcher_stat_object.war

def hitters_WAR_sum(hitters):
    total_WAR = 0
    for h in hitters:
        total_WAR += h.WAR()
    return total_WAR

def team_WAR(hitters, sp_war):
    return hitters_WAR_sum(hitters) + float(sp_war)