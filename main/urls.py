from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('news', views.news, name='news'),
    path('registration', views.registration, name='registration'),
    path('authorisation', views.auth, name='auth'),
    path('profile', views.profile, name='profile')

]
