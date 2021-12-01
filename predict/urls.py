from django.urls import path
from . import views

app_name = 'predict'

urlpatterns = [
    path('', views.match_list, name="predict"),
]