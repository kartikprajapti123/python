from django.shortcuts import render
# Create your views here.
from .models import singer,song
def index(request):
    
    songs=song.objects.all()
    context={
        'songs':songs,
    }
    return render(request,"index.html",context)


def detail(request,id):
    songs=song.objects.filter(pk=id).first()
    
    context={
        'song':songs
    }
    return render(request,"detail.html",context)

    