from django.db import models
import uuid

# Create your models here.

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=24)
    password = models.CharField(max_length=8)
    email = models.EmailField(max_length=50,unique=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    genre = models.CharField(max_length=150, null=True)
    rating = models.CharField(max_length=150, null=True)
    release_date = models.DateField()

    def __str__(self):
        return self.name

class Rating(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey("User", on_delete=models.CASCADE)
    movie_id = models.ManyToManyField("Movie", related_name="+")
    rating = models.FloatField()

    def __str__(self):
        return self.name
