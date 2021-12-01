from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.dateformat import DateFormat
from datetime import datetime, timedelta
from article.models import Articles

def date_range():
    today = DateFormat(datetime.now()).format('ymd')
    start = datetime.strptime(today, "%y%m%d") - timedelta(days=4)
    dates = [(start + timedelta(days=i)).strftime("20%y-%m-%d") for i in range(5)]
    return dates

def article_list(request):
    """
    article 출력
    """
    print("dsdsds")
    page = request.GET.get('page','1') #GET 방식으로 정보를 받아오는 데이터
    team_text = request.GET.get('team')
    date = request.GET.get('date')
    dates = date_range()
    if(date != None):
        date_conver = date.replace("-","")
    else:
        date_conver = dates[4].replace("-","")

    #dates[4] = 현재 날짜
    if(team_text != '전체' and team_text != None and date != None):
        article = Articles.objects.filter(team=team_text,date=date_conver)#.order_by('-written_time')
    #팀만 선택할 경우 기본 값으로 오늘로 가게된다.
    elif(team_text == None and date == None):
        article = Articles.objects.filter(date=date_conver)#.order_by('-written_time')
    elif(team_text == '전체' and date == None):
        article = Articles.objects.filter(date=date_conver)#.order_by('-written_time')
    elif(team_text == '전체' and date != None):
        article = Articles.objects.filter(date=date_conver)#.order_by('-written_time')
    else:
        article = Articles.objects.filter(team=team_text, date=date_conver)#.order_by('-written_time')

    #페이지네이션
    paginator = Paginator(article, '10') #Paginator(분할될 객체, 페이지 당 담길 객체수)
    article_list = paginator.page(page) #페이지 번호를 받아 해당 페이지를 리턴 get_page 권장

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
def reinforce(request,article_id):

    print(article_id)
    article = findArticle(article_id)
    print(article)
    article_texts = article['content'].split('.')
    context = {
        'article_texts': article_texts,
        'article': article,
     }
    return render(request, 'manager/manager_reinforce.html', context)


