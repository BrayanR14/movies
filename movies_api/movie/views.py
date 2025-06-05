#from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie.models import Movie
from movie.serializers import MovieSerializer


@api_view(["GET", "POST"]) 
def get_movie(request):

    if request.method == "GET":
        movies = Movie.objects.all()
        #data = []
        #for element in movies:
        #    data.append({
        #        'id': element.id,
        #        'title': element.title
        #    })
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=200)

    if request.method == "POST":
        return Response({}, status=201)

    return Response({}, status=405)