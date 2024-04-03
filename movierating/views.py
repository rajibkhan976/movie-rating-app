from rest_framework import generics
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer

# Create your views here.


class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all().order_by("-name")
    serializer_class = MovieSerializer
