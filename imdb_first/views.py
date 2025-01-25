from django.shortcuts import render
from imdb_first.models import Movie
from django.http import JsonResponse
# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()
    data = {
         'movies': list(movies.values())
         }
    return JsonResponse(data)

def movie_detail(request,pk):
    movie = Movie.objects.get(pk=pk)
    print(movie)
    data = {
         'name': movie.name,
         'description':movie.description,
         }
    return JsonResponse(data)
