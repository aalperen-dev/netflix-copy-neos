from django.urls import path
from .views import *

urlpatterns = [
    path('register/', userRegister, name = 'register'),
    path('login/',userLogin,name='login' ),
    path('profiles/',profiles,name='profiles'),
    path('olustur/', olustur ,name='olustur'),
    path('hesap/',hesap,name='hesap'),
    path('logout/',userLogout,name='logout'),
    path('delete/',hesapSil,name='delete'),
    path('dondur/',dondur,name='dondur')
]