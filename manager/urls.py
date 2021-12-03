from django.urls import path

from .views import article_list, judge_article, reinforce
# from article.views import article_list
# 앱 마다 명칭 다르게 하기
app_name = 'manager'

urlpatterns = [
    # article_views.py
    path('list/', article_list, name='article_list'),
    path('<article_id>/', judge_article, name='judge_article'),
    path('list/reinforce', reinforce, name='reinforce'),
]
