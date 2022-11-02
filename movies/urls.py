from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name ='index'),
    path('movies/<str:slugfield>/<str:profilID>',movies, name='movies'),
    path('search/', search, name='search'),
    path('video/<int:pk>', video, name='video')
]