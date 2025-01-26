from django.urls import path,include
#from imdb_first.api.views import movie_list,movie_detail
from imdb_first.api.views import MovieDetailAV,MovieListAV

urlpatterns = [
    path('list/',MovieListAV.as_view(),name='movie-list'),
    path('<int:pk>',MovieDetailAV.as_view(),name='movie-detail'),
]
