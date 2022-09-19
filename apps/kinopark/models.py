from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    producer = models.CharField(max_length=50, blank=False, default='')
    rating = models.FloatField(blank=False)
    published = models.BooleanField(default=False)


class Movie_details(models.Model):
    publishing_company = models.CharField(max_length=100, blank=False, default='')
    publication_date = models.DateTimeField()
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)

