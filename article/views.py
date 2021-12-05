from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import Articles
from datetime import datetime, timedelta
from django.utils.dateformat import DateFormat

def date_range():
    today = DateFormat(datetime(2021,9,22)).format('ymd') #날짜 변경 수정
    start = datetime.strptime(today, "%y%m%d") - timedelta(days=4)
    dates = [(start + timedelta(days=i)).strftime("20%y-%m-%d") for i in range(5)]
    return dates

# 기사 오류 해결
def article_list(request):
    page = request.GET.get('page','1') #GET 방식으로 정보를 받아오는 데이터
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

    #dates[4] = 현재 날짜
    if(team_text != '전체'):
        article = Articles.objects.filter(team=team_text,date=date)#.order_by('-written_time')
    #팀만 선택할 경우 기본 값으로 오늘로 가게된다.
    else:
        article = Articles.objects.filter(date=date)#.order_by('-written_time')

    #페이지네이션
    paginator = Paginator(article, '10') #Paginator(분할될 객체, 페이지 당 담길 객체수)
    article_list = paginator.page(page) #페이지 번호를 받아 해당 페이지를 리턴 get_page 권장

    if request.session.get('user'):
        id = request.session['user']
        context = {
                'id': id,
                'team_text': team_text,
                'article_list': article_list,
                'dates': dates,
                'date': date,
            }
    else:
        context = {
            'team_text': team_text,
            'article_list': article_list,
            'dates': dates,
            'date': date,
        }

    return render(request, 'article/article_list.html', context)
