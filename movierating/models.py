from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=24)
    password = models.CharField(max_length=8)
    email = models.EmailField(max_length=50,unique=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    genre = models.CharField(max_length=150, null=True)
    rating = models.CharField(max_length=150, null=True)
    release_date = models.DateField()

    def __str__(self):
        return self.name

class Rating(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="ids")
    movie_id = models.ForeignKey(
        "Movie", on_delete=models.CASCADE, related_name="ids")
    rating = models.FloatField()

    def __str__(self):
        return self.name
