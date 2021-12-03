from logic.find_keyword import *
from logic.make_wordcloud import load_predict_wordcloud
from logic.predict_with_article import get_contents, positive_score
from logic.predict_with_stat import get_players, make_hitter_objects, pitcher_WAR, team_WAR
from predict.models import Starting_lineup, Pitcher_stats, Hitter_stats
from article.models import Articles
import datetime
import os

def before_day_str(date, period):
    datetype = datetime.datetime.strptime(date, "%Y%m%d")
    before = datetype - datetime.timedelta(days=int(period))
    before = before.strftime("%Y%m%d")
    print(date, before)
    return before

def article_based(away, home, period, date):
    before = before_day_str(date, period)
    if away == "SSG":
        away = "SK"
    if home == "SSG":
        home = "SK"
    away_articles_objects = Articles.objects.filter(team=away, date__gte=before, date__lte=date)
    away_articles = get_contents(away_articles_objects)
    away_score = positive_score(away_articles)
    home_articles_objects = Articles.objects.filter(team=away, date__gte=before, date__lte=date)
    home_articles = get_contents(home_articles_objects)
    home_score = positive_score(home_articles)

    away_whole_keyword = ''
    home_whole_keyword = ''

    if away == "SK":
        away = "SSG"
    if home == "SK":
        home = "SSG"

    path = 'C:/Users/DeepLearning_1/PycharmProjects/WindUp/static/img/predict/'

    if not os.path.exists(path + away + date + '_' + period + '.png'):
        for a in away_articles:
            tenkey = top10keywords(a)
            away_whole_keyword += arr2str(tenkey)
        load_predict_wordcloud(away, away_whole_keyword, date, period)

        for h in home_articles:
            tenkey = top10keywords(h)
            home_whole_keyword += arr2str(tenkey)
        load_predict_wordcloud(home, home_whole_keyword, date, period)

    if away_score > home_score:
        return away
    else:
        return home

def stat_based(away, home, date):
    away_lineup_objects = Starting_lineup.objects.filter(date=date, team=away)
    away_lineup = get_players(away_lineup_objects)
    home_lineup_objects = Starting_lineup.objects.filter(date=date, team=home)
    home_lineup = get_players(home_lineup_objects)

    # print('원정:', away_lineup)
    # print('홈:', home_lineup)

    away_sp = away_lineup[0]
    away_hitters = away_lineup[1:]
    home_sp = home_lineup[0]
    home_hitters = home_lineup[1:]

    away_sp_stat = Pitcher_stats.objects.get(name=away_sp, team=away, opposite_team=home)
    home_sp_stat = Pitcher_stats.objects.get(name=home_sp, team=home, opposite_team=away)
    away_sp_war = pitcher_WAR(away_sp_stat)
    home_sp_war = pitcher_WAR(home_sp_stat)

    away_hitters_objects = make_hitter_objects(away_hitters, away, home)
    home_hitters_objects = make_hitter_objects(home_hitters, home, away)

    away_team_WAR = team_WAR(away_hitters_objects, away_sp_war)
    home_team_WAR = team_WAR(home_hitters_objects, home_sp_war)

    if away_team_WAR > home_team_WAR:
        return away
    else:
        return home


def both_based(away, home):
    return