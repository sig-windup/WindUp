from bson import ObjectId
from django.forms import model_to_dict
from django.shortcuts import render, get_object_or_404, redirect
import datetime
from django.utils.dateformat import DateFormat
from pymongo import MongoClient
from home.models import *
from logic.make_wordcloud import load_highlight_wordcloud
from predict.models import *
from logic.predict import *
from article.models import Articles
from users.models import User
from django.db.models import Q

# Create your views here.
def match_list(request) :
    today = DateFormat(datetime.datetime(2021,9,22)).format('Ymd')
    date = request.GET.get('dates')
    game = request.GET.get('game')

    if date is None or date == '' :
        # 시작일 지정
        date_conver = today
    else :
        date_conver = date.replace("-", "")
    matches = Matches.objects.filter(date=date_conver).order_by('id')

    if game is not None:
        game_info = findMatch(game)
        away = game_info['away']
        home = game_info['home']
        period = request.GET.get('period')
        if period is None:
            period = "1"
    else:
        if request.session.get('user'):
            id = request.session['user']
            user = User.objects.get(user_id=id)
            favorite_team = Teams.objects.get(team_id=user.team_id)
            favorite_team_text = favorite_team.team_code
            game_info = Matches.objects.get(Q(date=date_conver), Q(away=favorite_team_text) | Q(home=favorite_team_text))
        else:
            game_info = matches[0]
        game_info = model_to_dict(game_info)
        away = game_info['away']
        home = game_info['home']
        period = request.GET.get('period')
        if period is None:
            period = "1"

    away_team_obj = Teams.objects.get(team_code=away)
    home_team_obj = Teams.objects.get(team_code=home)

    if game_info['state_game'] == '':
        article_upper, away_positive_score, home_positive_score = article_based(away, home, period, date_conver)
        datetype = datetime.datetime.strptime(today, "%Y%m%d")
        before = datetype - datetime.timedelta(days=1)
        before = before.strftime("%Y%m%d")
        stat_upper, away_war, home_war = stat_based(away, home, before)

        both_upper, winning_rate = both_based(away_positive_score, home_positive_score, away_war, home_war)
        print('승리확률 높은 팀은', both_upper, '확률은', winning_rate*100)
        winning_rate *= 100
        winning_rate = round(winning_rate, 1)
        print(away_team_obj.team_name, home_team_obj.team_name)
        if request.session.get('user'):
            id = request.session['user']
            context = {
                'id': id,
                'matches': matches,
                'game_info': game_info,
                'period': period,
                'date': date,
                'article_upper': article_upper,
                'stat_upper': stat_upper,
                'both_upper': both_upper,
                'winning_rate': winning_rate,
                'opposite_rate': 100 - winning_rate,
                'away_team_obj': away_team_obj,
                'home_team_obj': home_team_obj,
            }
        else:
            context = {
                'matches': matches,
                'game_info': game_info,
                'period': period,
                'date': date,
                'article_upper': article_upper,
                'stat_upper': stat_upper,
                'both_upper': both_upper,
                'winning_rate': winning_rate,
                'opposite_rate': 100 - winning_rate,
                'away_team_obj': away_team_obj,
                'home_team_obj': home_team_obj,
            }
    else:
        if away == "SSG":
            away = "SK"
        if home == "SSG":
            home = "SK"
        path = 'C:/Users/DeepLearning_1/PycharmProjects/WindUp/static/img/highlight/'
        if not os.path.exists(path + away + date_conver + '.png'):
            articles = Articles.objects.filter(team=away, date=date_conver)
            if away == "SK":
                away = "SSG"
            whole_keyword = ''
            for a in articles:
                print(a)
                tenkey = top10keywords(a.content)
                whole_keyword += arr2str(tenkey)
            print('키워드', whole_keyword)
            load_highlight_wordcloud(away, whole_keyword, date_conver)

        if not os.path.exists(path + home + date_conver + '.png'):
            articles = Articles.objects.filter(team=home, date=date_conver)
            if home == "SK":
                home = "SSG"
            whole_keyword = ''
            for a in articles:
                tenkey = top10keywords(a.content)
                whole_keyword += arr2str(tenkey)
            load_highlight_wordcloud(home, whole_keyword, date_conver)
        if request.session.get('user'):
            id = request.session['user']
            context = {
                'id': id,
                'matches': matches,
                'game_info': game_info,
                'period': period,
                'date': date,
                'away_team_obj': away_team_obj,
                'home_team_obj': home_team_obj,
            }
        else:
            context = {
                'matches': matches,
                'game_info': game_info,
                'period': period,
                'date': date,
                'away_team_obj': away_team_obj,
                'home_team_obj': home_team_obj,
            }
    return render(request, 'predict/predict.html', context)

def findMatch(match_id):
    mongo=MongoClient("mongodb://windup_dba:lotsamhwa@114.129.200.203:28018")
    db=mongo['windup']
    col=db['matches']
    return col.find_one({'_id':ObjectId(match_id)})