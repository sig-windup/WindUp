import os

from django.shortcuts import render

from home.models import Matches, Teams
from article.models import Articles
from logic.make_wordcloud import load_highlight_wordcloud
from logic.find_keyword import top10keywords, arr2str


def index(request):
    #stategame이 없을 경우 게임예정이다 -> score, result 모두 에도 점수가 없다.

    date = "20210922"
    matches = Matches.objects.filter(date=date)

    path = 'C:/Users/DeepLearning_1/PycharmProjects/WindUp/static/img/highlight/'

    if not os.path.exists(path + '전체' + date + '.png'):
        articles = Articles.objects.filter(date=date)
        whole_keyword = ''
        for a in articles:
            tenkey = top10keywords(a.content)
            whole_keyword += arr2str(tenkey)
        load_highlight_wordcloud('전체', whole_keyword, date)

    if request.session.get('user'):
        id = request.session['user']
        context = {
                'id': id,
                'matches': matches,
                # 'img': img,
                'date': date,
        }
    else:
        context = {
                'matches': matches,
                # 'img': img,
                'date': date,
        }

    return render(request, 'home/home.html', context)

