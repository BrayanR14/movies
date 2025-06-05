from django.urls import path
from movie.views import get_movie

app_name = 'movie'
urlpatterns = [
    path('', get_movie, name='movie'),    
]