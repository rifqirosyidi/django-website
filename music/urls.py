from django.urls import path
from .import views

app_name = 'music'
urlpatterns = [
    path('register/', views.UserFormView.as_view(), name='register'),

    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('album/add', views.AlbumCreate.as_view(), name='album-create'),
    path('album/<int:pk>/update', views.AlbumUpdate.as_view(), name='album-update'),
    path('album/<int:pk>/delete', views.AlbumDelete.as_view(), name='album-delete'),
]
