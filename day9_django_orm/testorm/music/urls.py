from django.urls import path
from . import views
from .views import album_list, create_album, update_album, delete_album

urlpatterns = [
    path('', views.album_list, name='album_list'),
    path('add/',create_album, name='create_album'),
    path('edit/<int:pk>/', update_album, name='update_album'),
    path('delete/<int:pk>', delete_album, name='delete_album'),
]