from django.urls import reverse_lazy
from django.views import generic
from .models import Album, Song


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'album_list'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(generic.CreateView):
    model = Album
    fields = '__all__'


class AlbumUpdate(generic.UpdateView):
    model = Album
    fields = '__all__'


class AlbumDelete(generic.DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')
