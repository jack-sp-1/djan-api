from imdb_first.models import Movie
from imdb_first.api.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method=='GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    
@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request,pk):
    if request.method == 'GET':
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
                
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    if request.method == 'PUT':
         movie = Movie.objects.get(pk=pk)
         serializer = MovieSerializer(movie, data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
         else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
         movie = Movie.objects.get(pk=pk)
         movie.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)
    
