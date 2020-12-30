from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import News
from .forms import RegistrationForm


def index(request):
    return render(request, 'main/index.html')


def news(request):
    adminNews = News.objects.all()
    return render(request, 'main/news.html', {'title': 'Новости', 'news': adminNews})


def profile(request):
    return render(request, 'main/profile.html')


def registration(request):
    data = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            data['form'] = form
            data['res'] = "Все прошло успешно"
            return redirect('/')
    else:
        form = RegistrationForm()
        data['form'] = form
        return render(request, 'main/registration.html', data)
    return render(request, 'main/registration.html', data)