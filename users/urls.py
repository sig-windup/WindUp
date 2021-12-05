from django.urls import path
from . import views

app_name = 'users'

urlpatterns= [
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('join/', views.join_view, name="join"),
    path('update/', views.update_view, name='update'),
    path('delete/', views.delete_view, name='delete'),
]
