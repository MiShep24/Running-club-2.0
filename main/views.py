from django.shortcuts import render
from django.http import HttpResponse
from .models import News


def index(request):
    return render(request, 'main/index.html')


def news(request):
    adminNews = News.objects.all()
    return render(request, 'main/news.html', {'title': 'Новости', 'news': adminNews})


def profile(request):
    return render(request, 'main/profile.html')
