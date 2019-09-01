from django.http import HttpResponse
from django.shortcuts import render
from .models import Album, Song


# Create your views here.
def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    return render(request, 'music/index.html', context)


def detail(request, pk):
    return HttpResponse("Details for album_id : " + str(pk))
