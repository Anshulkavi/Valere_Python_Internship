from django import forms
from .models import Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'artist', 'genre']

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['name', 'singer', 'album']