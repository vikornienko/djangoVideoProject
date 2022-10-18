import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

AGE_CHOICES = (
    ('All', 'All'),
    ('Kids', 'Kids')
)

MOVIE_CHOICES = (
    ('seasonal', 'Seasonal'),
    ('single', 'Single')
)

class CustomUser(AbstractUser):
    profiles = models.ManyToManyField('Profile', null=True, blank=True)

class Profile(models.Model):
    name = models.CharField(max_length=32)
    age_limit = models.CharField(max_length=10, choices=AGE_CHOICES)
    uuid_profile = models.UUIDField(default=uuid.uuid4)

class Movie(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    uuid_movie = models.UUIDField(default=uuid.uuid4)
    type_movie = models.CharField(max_length=10, choices=MOVIE_CHOICES)
    videos = models.ManyToManyField('Video')
    flyer = models.ImageField(upload_to='flyers')
    age_limit = models.CharField(max_length=10, choices=AGE_CHOICES)

class Video(models.Model):
    title = models.CharField(max_length=128, blank=True, null=True)
    file = models.FileField(upload_to='movies')

