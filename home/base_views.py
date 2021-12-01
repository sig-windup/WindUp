from django.shortcuts import render, get_object_or_404


def index(request):
    """
    post 목록 출력
    """
    return render(request, 'home/home.html')
