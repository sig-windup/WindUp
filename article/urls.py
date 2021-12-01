from django.urls import path

# 앱 마다 명칭 다르게 하기
from .views import article_list
# 앱 마다 명칭 다르게 하기
app_name = 'article'
urlpatterns = [
    # article_views.py
    path('', article_list, name='article_list'),
]