from django.shortcuts import get_object_or_404, redirect
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from .models import Movie, User
from .serializers import *

# Create your views here.


class LoginView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'login.html'

    def get(self, request):
        serializer = LoginSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        user = None
        serializer = LoginSerializer(data=request.data)
        try:
            user = User.objects.get(email=request.data['email'])
        except User.DoesNotExist:
            return Response({'serializer': serializer})
        if user and user.password == request.data['password']:
            request.session['user_id'] = user.id
        else:
            return redirect('login')
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        if request.session.get('user_id'):
            return redirect('movies')
        else:
            return redirect('login')


class AddMovieView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'add_movie.html'

    def get(self, request):
        if not request.session.get('user_id'):
            return redirect('login')
        serializer = AddMovieSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = AddMovieSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('movies')


class RateMovieView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'rate_movie.html'

    def get(self, request):
        if not request.session.get('user_id'):
            return redirect('login')
        serializer = RateMovieSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = RateMovieSerializer(
            data=request.data, context={'request': request})
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('movies')


class MovieListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'movie_list.html'

    def get(self, request):
        if not request.session.get('user_id'):
            return redirect('login')
        queryset = Movie.objects.all().order_by("-name")
        serializer = SearchMovieSerializer()
        return Response({'serializer': serializer, 'movies': queryset})

    def post(self, request):
        if not request.session.get('user_id'):
            return redirect('login')
        queryset = Movie.objects.filter(name=request.data["search"])
        if not queryset:
            queryset = Movie.objects.all().order_by("-name")
        serializer = SearchMovieSerializer()
        return Response({'serializer': serializer, 'movies': queryset})
