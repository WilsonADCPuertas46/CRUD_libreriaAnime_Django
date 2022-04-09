from django.shortcuts import render, redirect, get_object_or_404
from .models import Anime
from .form import AnimeForm

def index(request):
    return render(request, 'index.html')


def information(request):
    return render(request, 'information.html')


def register(request):
    animes = Anime.objects.all()
    return render(request, 'librery_form/register.html', {'animes': animes})


def create(request):
    if request.method == 'POST':
        formaAnime = AnimeForm(request.POST or None, request.FILES or None)
        if formaAnime.is_valid():
            formaAnime.save()
            return redirect('register')
    else:
        formaAnime = AnimeForm()

    return render(request, 'librery_form/create.html', {'formaAnime': formaAnime})


def update(request, id):
    anime = get_object_or_404(Anime, pk=id)
    if request.method == 'POST':
        formaAnime = AnimeForm(request.POST or None, request.FILES or None, instance=anime)
        if formaAnime.is_valid():
            formaAnime.save()
            return redirect('register')

    else:
        formaAnime= AnimeForm(instance=anime)

    return render(request, 'librery_form/update.html', {'formaAnime': formaAnime})


def delete(request, id):
    anime = get_object_or_404(Anime, pk=id)
    anime.delete()
    return redirect('register')
