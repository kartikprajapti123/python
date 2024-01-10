from django.shortcuts import render
from .models import song
# Create your views here.
def index(request):
    songs=song.objects.all()
    
    return render(request,"index.html",context={'songs':songs})

def details(request,id):
    print("hello")
    songs=song.objects.get(pk=id)
    return render(request,"detail.html",context={'song':songs})