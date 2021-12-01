from django.urls import path
from . import views

# 앱 마다 명칭 다르게 하기
app_name = 'home'

urlpatterns = [
    # base_views.py
    path('', views.index, name='index'),
]
