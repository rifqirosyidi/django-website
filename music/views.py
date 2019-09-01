from django.shortcuts import render
from django.http import HttpResponse
from .models import Album, Song


# Create your views here.
def index(request):
    all_albums = Album.objects.all()
    html = ''
    for album in all_albums:
        album_id = str(album.id)
        html += '<a href="/music/' + album_id + '/">' + album.album_title + '</a>?'

    return HttpResponse(html)


def detail(request, pk):
    return HttpResponse("Details for album_id : " + str(pk))
