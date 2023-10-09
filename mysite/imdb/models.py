from django.db import models


class Director(models.Model):
    name = models.TextField(primary_key=True, max_length=100)


class Movie(models.Model):
    movie_id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    box_office_collection_in_crores = models.FloatField()
    director = models.ForeignKey(
        Director, on_delete=models.CASCADE, null=False)


class Actor(models.Model):
    actor_id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)


class Cast(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
    is_debut_movie = models.BooleanField(default=False)


class Rating(models.Model):
    movie = models.OneToOneField(
        Movie, on_delete=models.CASCADE)
    rating_one_count = models.IntegerField(default=0)
    rating_two_count = models.IntegerField(default=0)
    rating_three_count = models.IntegerField(default=0)
    rating_four_count = models.IntegerField(default=0)
    rating_five_count = models.IntegerField(default=0)
