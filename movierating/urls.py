from django.urls import path
from . import views

urlpatterns = [
    path("movies/", views.MovieListView.as_view(), name="movies"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("add-movie/", views.AddMovieView.as_view(), name="add-movie"),
    path("rate-movie/", views.RateMovieView.as_view(), name="rate-movie"),
]