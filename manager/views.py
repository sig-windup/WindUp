from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.dateformat import DateFormat
from datetime import datetime, timedelta
from article.models import Articles
from logic.store_judge import storeDB, makeCSV, start_reinforce

def date_range():
    today = DateFormat(datetime(2021,9,22)).format('ymd')
    start = datetime.strptime(today, "%y%m%d") - timedelta(days=4)
    dates = [(start + timedelta(days=i)).strftime("20%y-%m-%d") for i in range(5)]
    return dates

def article_list(request):
    """
    article 출력
    """
    page = request.GET.get('page', '1')  # GET 방식으로 정보를 받아오는 데이터
    team_text = request.GET.get('team')
    date = request.GET.get('date')
    print(date, type(date))
    dates = date_range()

    if (date == None):
        date = dates[3]
    else:
        if (date == 'None'):
            date = dates[3]
    date = date.replace("-", "")

    if (team_text == None):
        team_text = '전체'
    else:
        if (team_text == 'None'):
            team_text = '전체'

    # dates[4] = 현재 날짜
    if (team_text != '전체'):
        article = Articles.objects.filter(team=team_text, date=date)  # .order_by('-written_time')
    # 팀만 선택할 경우 기본 값으로 오늘로 가게된다.
    else:
        article = Articles.objects.filter(date=date)  # .order_by('-written_time')

    # 페이지네이션
    paginator = Paginator(article, '10')  # Paginator(분할될 객체, 페이지 당 담길 객체수)
    article_list = paginator.page(page)  # 페이지 번호를 받아 해당 페이지를 리턴 get_page 권장


    context = {
            'team_text': team_text,
            'article_list': article_list,
            'dates': dates,
         }

    return render(request, 'manager/manager_articleList.html', context)

from pymongo import MongoClient
from bson.objectid import ObjectId

def findArticle(article_id):
    mongo = MongoClient("mongodb://windup_dba:lotsamhwa@114.129.200.203:28018")
    db = mongo['windup']
    col = db['articles']
    return col.find_one({'_id': ObjectId(article_id)})

#강화학습
count = 0
myjudge = []
def judge_article(request, article_id):
    global count
    article = findArticle(article_id)
    article_texts = article['content'].split('.')
    if request.method == 'POST':
        if count != len(article_texts)-1:
            count+=1
        else:
            count = 0
            for i in range(len(myjudge)):
                print(article_texts[i], myjudge[i])
            storeDB(article_texts, myjudge)
            return redirect('/manager/list')
        choice = request.POST['judge']
        label_dict = {'중립': 0, '긍정': 1, '부정': 2}
        myjudge.append(label_dict[choice])

    context = {
        'article_texts': article_texts[int(count)],
        'article': article,
    }

    return render(request, 'manager/manager_reinforce.html', context)


def reinforce(request):
    makeCSV()
    start_reinforce()
    return redirect('/manager/list')

