from django.urls import path
from . import views
from .views import album_list, create_album, update_album, delete_album,
                   song_list, add_song, update_song, delete_song

urlpatterns = [
    path('', views.album_list, name='album_list'),
    path('add/',create_album, name='create_album'),
    path('edit/<int:pk>/', update_album, name='update_album'),
    path('delete/<int:pk>/', delete_album, name='delete_album'),
    path('', views.song_list, name='song_list')
    path('add/', add_song, name='add_song')
    path('update/<int:pk>/', update_song, name='update_song')
    path('delete/<int:pk>/', delete_song, name'delete_song')
]