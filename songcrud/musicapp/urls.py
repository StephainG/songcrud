from django.urls import path
from .views import ArtistesView, artistes_detail, SongsView, songs_detail, LyricsView, lyrics_detail

urlpatterns = [
    path('artistes/', ArtistesView),
    path('details/<int:pk>', artistes_detail),
    #path('genericApiView/', genericApiView.as_view())
    path('songs/', SongsView),
    path('detailss/<int:pk>', songs_detail),
    path('lyrics/', LyricsView),
    path('detail/<int:pk>', lyrics_detail)
]