from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import News
from .forms import RegistrationForm, UserForm, ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import connection, transaction
from django.contrib import messages
from django.template import RequestContext


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
        print('pachemy')
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
        print(type(user))
        if user is not None:
            login(request, user)
            return redirect('profile/{}'.format(request.user.username))

    return render(request, 'main/auth.html', data)


@login_required
def profile(request, username):
    active_person = request.user.username
    if str(active_person) == username:
        all_student = User.objects.all()
        for student in all_student:
            if str(student) == username:
                logStudent = student
    #    print(type(logStudent))
        title = str(logStudent.first_name) + ' ' + str(logStudent.last_name)
        return render(request, 'main/profile.html', {'title': title, 'logStudent': logStudent, 'username': username})
    else:
        all_student = User.objects.all()
        for student in all_student:
            if str(student) == username:
                logStudent = student
        #    print(type(logStudent))
        title = str(logStudent.first_name) + ' ' + str(logStudent.last_name)
        return render(request, 'main/profile.html', {'title': title, 'logStudent': logStudent})


@login_required
def leave_profile(request):
    logout(request)
    return redirect('/')


@login_required
@transaction.atomic
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
#    return render(request, 'main/edit_profile.html')


