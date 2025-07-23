from django.shortcuts import render, redirect
from .models import Album, Song
from .forms import AlbumForm, SongForm
from django.shortcuts import get_object_or_404
# Create your views here.

def album_list(request):
    albums = Album.objects.all()
    return render(request, 'music/album_list.html', {'albums': albums})

def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('album_list')
    else:
        form = AlbumForm()
    return render(request,  'music/create_album.html', {'form': form})    

def update_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_list')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'music/update_album.html', {'form': form})             

def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect('album_list')
    return render(request, 'music/delete_album.html', {'albums': album})    

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'music/song_list.html', {'songs': songs})

def add_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('song_list')
    else:
        form = SongForm()
    return render(request, 'music/add_song.html', {'form': form})

def update_song(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'POST':
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            form.save()
            return redirect('song_list')
    else:
        form = SongForm()
    return render(request, 'music/update_song.html', {'form': form})

def delete_song(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'POST':
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            form.save()
            return redirect('song_list')
    else:
        form = SongForm()
    return render(request, 'music/delete_song.html', {'form': form})                                