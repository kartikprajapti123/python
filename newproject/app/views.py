from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, genre
# Create your views here.
def index(request):
    movies=Movie.objects.all()
    context={
        'movies':movies
    }
    return render(request,"index.html",context)


def details(request,id):
    movie=Movie.objects.filter(pk=id).first()
    print(movie)
    context={
        'movie':movie
    }
    return render(request,"detail.html",context)