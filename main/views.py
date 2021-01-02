from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import News
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'main/index.html')


def news(request):
    adminNews = News.objects.all()
    listNews = adminNews.order_by('-id')
    return render(request, 'main/news.html', {'title': 'Новости', 'listNews': listNews})


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


def auth(request):
    data = {}
    if request.method == 'POST':
        fm = AuthenticationForm(request, request.POST)
        if fm.is_valid():
            user_name = fm.cleaned_data['username']
            user_pass = fm.cleaned_data['password']
            user = authenticate(user_name, user_pass)
            data['fm'] = fm
            data['res'] = "Успешно!"
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('profile')
        else:
            fm = AuthenticationForm()
            data['fm'] = fm
            return render(request, 'main/auth.html')

    return render(request, 'main/auth.html')


def profile(request):
    return render(request, 'main/profile.html')
