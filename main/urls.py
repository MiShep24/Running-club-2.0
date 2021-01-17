from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('news', views.news, name='news'),
    path('registration', views.registration, name='registration'),
    path('authorisation', views.auth, name='auth'),
    path('logout', views.leave_profile, name='leave_profile'),
    path('profile/<str:username>', views.profile, name='profile'),
    path('edit_profile', views.edit_profile, name='edit'),

]
