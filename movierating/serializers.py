from rest_framework import serializers
from .models import *
from django.contrib.sessions.models import Session


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
        max_length=50,
        style={'placeholder': 'Email', 'autofocus': True}
    )
    password = serializers.CharField(
        max_length=8,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class AddMovieSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    genre = serializers.CharField(max_length=150)
    rating = serializers.CharField(max_length=150)
    release_date = serializers.DateField(style={'input_type': 'date'})

    def create(self, validated_data):
        movie = Movie.objects.create(**validated_data)
        return movie


class RateMovieSerializer(serializers.Serializer):
    movie_id = serializers.PrimaryKeyRelatedField(
        queryset=Movie.objects.all())
    rating = serializers.IntegerField(style={'input_type': 'number'})

    def create(self, validated_data):
        validated_data["user_id"] = User.objects.get(id=self.context.get(
            "request").session.get('user_id'))
        rate = Rating.objects.create(**validated_data)
        return rate


class SearchMovieSerializer(serializers.Serializer):
    search = serializers.CharField(
        max_length=150)
