
from django.shortcuts import render,redirect

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import *

from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def userRegister(request):
    if request.method == 'POST':
        kullanici = request.POST['kullanici']
        email = request.POST['email']
        tel = request.POST['tel']
        resim = request.FILES['resim']
        sifre1 = request.POST['sifre1']
        sifre2 = request.POST['sifre2']

        if kullanici != '' and email != '' and sifre1 !=' ':
            if sifre1 == sifre2:
                if User.objects.filter(username = kullanici).exists():
                    messages.error(request,'Bu kullanici adı alınmış')
                    return redirect('register')
                elif User.objects.filter(email = email).exists():
                    messages.error(request,'bu e posta kullanımda')
                    return redirect('register')
                elif len(sifre1)< 6:
                    messages.error(request,'Şifre 6 karakterden kısa olamaz!!')
                    return redirect('register')
                elif kullanici in sifre1:
                    messages.error(request,'Kullanici adi ve şifre benzer')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username = kullanici, email=email, password=sifre1)
                    Hesap.objects.create(
                        user = user,
                        resim = resim,
                        tel = tel
                    )
                    
                    subject = '12 eylul'
                    message = f"merhaba {kullanici}. !!!"
                    send_mail(
                        subject,
                        message,
                        settings.EMAIL_HOST_USER,
                        [email]
                    )
                    user.save()
                    messages.success(request,'Üyelik başarılı!!!')
                    return redirect('index')
            else:
                messages.error(request, 'Şifreler uyumsuz!!!')
                return redirect('register')
        else:
            messages.error(request, 'Tüm alanların oldurulması zorunludur!!!')
            return redirect('register')
    return render (request,'user/register.html')

def userLogin(request):
    if request.method == 'POST':
        username = request.POST['kullanici']
        password = request.POST['password']

        user = authenticate(request, username= username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request,'Giriş başarılı!!!')
            return redirect('profiles')
        else:
            messages.error(request,'Kullanici adi vey şifre hatali!!!')
            return redirect('login')
    return render(request, 'user/login.html')

def profiles(request):
    profiller = Profil.objects.filter(user = request.user)
    context = {
        'profiller':profiller
    }
    return render(request,'user/browse.html',context)

def olustur(request):
    form = ProfilForm()
    if request.method == 'POST':
        form = ProfilForm(request.POST, request.FILES)
        if form.is_valid():
            if Profil.objects.filter(user = request.user).count() < 4:
                profil = form.save(commit=False)
                profil.user = request.user
                profil.save()
                messages.success(request,'profil oluşturuldu!!!')
                return redirect('profiles')
            else:
                messages.error(request,'en fazla 4 profil oluşturabilirisiniz!!!')
    context = {
        'form': form
    }
    return render(request,'user/olustur.html',context)

def hesap(request):
    user = request.user.hesap
    context = {
        'user': user
    }
    return render (request, 'user/hesap.html',context)

def userLogout(request):
    logout(request)
    messages.success(request,'çıkış başarılı')
    return redirect('index')

def hesapSil(request):
    user = request.user
    user.delete()
    messages.success(request,'üyelik silindi')
    return redirect('index')

def dondur(request):
    user = request.user
    user.is_active = False
    user.save()
    messages.success(request,'hesap donduruldu. tekrar aktifleştirmek isterseniz iletişime geçin.')
    return redirect('index')
