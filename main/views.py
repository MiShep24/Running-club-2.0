import json
import requests
from bs4 import BeautifulSoup
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render, redirect

from .forms import RegistrationForm, UserForm, ProfileForm
from .models import News, Profile, RunPosts


def index(request):
    return render(request, 'main/index.html')


def news(request):
    adminNews = News.objects.all()
    listNews = adminNews.order_by('-id')
    print(listNews)
    return render(request, 'main/news.html', {'title': 'Новости', 'listNews': listNews})


def registration(request):
    data = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            data['form'] = form
            data['res'] = "Все прошло успешно"
            print(data['res'])
            return redirect('auth')
    else:
        form = RegistrationForm()
        data['form'] = form
        return render(request, 'main/registration.html', data)
    return render(request, 'main/registration.html', data)


def auth(request):
    data = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile/{}'.format(request.user.username))

    return render(request, 'main/auth.html', data)


@login_required
def profile(request, username):
    active_person = request.user.username
    if str(active_person) == username:
        posts = RunPosts.objects.all().filter(user=request.user)
        list_posts = posts.order_by("-id")
        all_student = User.objects.all()
        for student in all_student:
            if str(student) == username:
                logStudent = student
        title = str(logStudent.first_name) + ' ' + str(logStudent.last_name)

        return render(request, 'main/profile.html', {'title': title, 'logStudent': logStudent, 'username': username,
                                                     'list_posts': list_posts})
    else:
        all_student = User.objects.all()
        for student in all_student:
            if str(student) == username:
                logStudent = student
        posts = RunPosts.objects.all().filter(user=logStudent)
        list_posts = posts.order_by("-id")
        title = str(logStudent.first_name) + ' ' + str(logStudent.last_name)
        return render(request, 'main/profile.html', {'title': title, 'logStudent': logStudent,
                                                     'list_posts': list_posts})


@login_required
def leave_profile(request):
    logout(request)
    return redirect('/')


@login_required
@transaction.atomic
def edit_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('profile', request.user.username)
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'main/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


@login_required
def new_post(request, username):
    if request.method == 'POST':
        url = request.POST.get('train_link')

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        item = soup.select_one("[data-react-class='ActivityPublic']")
        name_train = json.loads(item.get("data-react-props"))['activity']['name']
        time_quotes = json.loads(item.get("data-react-props"))['activity']['date']
        name_student = json.loads(item.get("data-react-props"))['activity']['athlete']['name']
        run_distance = json.loads(item.get("data-react-props"))['activity']['distance']
        run_time = json.loads(item.get("data-react-props"))['activity']['time']
        active_name = request.user.first_name + ' ' + request.user.last_name
        if item is None:
            messages.error(request, "Too many requests!")
            return redirect('profile', username)

        if active_name == name_student:
            RunPosts.objects.create(name=name_train, link_post=url, distance=run_distance, run_time=run_time,
                                    date_running=time_quotes, user=request.user)
        else:
            messages.error(request, "Это не ваша тренировка!")
        return redirect('profile', username)

    except:
        messages.error(request, "Неверная ссылка! Ссылка должна содержать информацию о тренировке! Пример ссылки: "
                                "https://www.strava.com/activities/<id_activities>")
        return redirect('profile', username)


def all_profiles(request):
    all_users = User.objects.all()
    list_users = all_users.order_by("username")
    return render(request, 'main/all_users.html', {'title': 'Все пользователи', 'list_users': list_users})
