import profile
from django.shortcuts import render,redirect
from .models import*
from user.models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def movies(request, profilID, slugfield):
    # filmler = Movie.objects.all()
    profil = Profil.objects.filter(slug = slugfield).get(id = profilID)
    populer = Movie.objects.filter(kategori__isim = 'populer')
    gundem = Movie.objects.filter(kategori__isim = 'gundem')
    profiller = Profil.objects.filter(user = request.user)
    context = {
        'populer':populer,
        'gundem':gundem,
        'profil': profil,
        'profiller':profiller
    }
    return render(request, 'browse-index.html',context)

def search(request):
    filmler = ''
    search =''
    profiller = Profil.objects.filter(user = request.user)
    if request.GET.get('search'):
        search = request.GET.get('search')
        filmler = Movie.objects.filter(isim__icontains = search)

    context = {
        'filmler':filmler,
        'search':search,
        'profiller':profiller
    }
    return render(request,'search.html',context)

def view_404(request, exception):
    return redirect('/')

def video(request, pk):
    video = Movie.objects.get(id = pk)
    context = {
        'video':video
    }
    return render (request,'video.html', context)