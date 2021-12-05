from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import urllib
# Create your views here.

def login_view(request) :
    if request.method == "POST" :
        user_id = request.POST["user_id"]
        user_pwd = request.POST['user_pwd']

        try :
            user = User.objects.get(user_id=user_id, password = user_pwd)
            if user is not None :
                context = {
                    'id' : user_id,
                }
                request.session['user'] = user.user_id
                return redirect('/home')
            else :
                context = {
                    'error' :"회원없음.",
                }
                return render(request, 'users/login.html')
        except Exception as e :
            print(e)
            return render(request, 'users/login.html')
    return render(request, 'users/login.html')


def logout_view(request) :
    if request.session.get('user') :
        del(request.session['user'])
    return redirect('users:login')

def join_view(request) :
    if request.method == "POST" :
        user_id = request.POST["user_id"]
        user_pwd = request.POST["user_pwd"]
        team_name = request.POST['team']

        id = User.objects.filter(user_id = user_id).values("user_id")
        try :
            if id[0]['user_id'] :
                messages.warning(request, "이미 사용중인 id 입니다.")
        except Exception as e :
            print(e)
            messages.warning(request, "사용가능한 id 입니다.")

            user = User()
            user.user_id = user_id
            user.team_id = team_name
            user.password = user_pwd
            user.save()
            return redirect('users:login')
    return render(request, "users/join.html")

def update_view(request) :
    if request.session.get('user'):
        id = request.session['user']
        if request.method == "POST" :
            user_pwd = request.POST["user_pwd"]
            team_name = request.POST["team"]
            user = User()
            user.user_id = id
            user.team_id = team_name
            user.password = user_pwd
            user.save()
            return redirect('/home')
    return render(request, "users/update.html")


def delete_view(request) :
    if request.session.get('user') :
        id = request.session['user']

        user = User.objects.filter(user_id = id)
        user.delete()
        logout_view(request)
        messages.success(request, "탈퇴완료")
        return redirect('users:login')
    return render(request, 'users/delete.html')