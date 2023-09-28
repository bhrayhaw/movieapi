from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class StreamPlatform(models.Model):
    name = models.CharField(max_length=90)
    description = models.CharField(max_length=155)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    platform = models.ForeignKey(
        StreamPlatform, on_delete=models.CASCADE, related_name="watchlist_platforms")
    is_released = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Reviews(models.Model):
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=255)
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name="movie_review")
    active = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.movie.title + " is a " + str(self.rating) + " " + "star rated Movie"
