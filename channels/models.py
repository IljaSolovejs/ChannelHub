from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

GENRE_CHOICES = [
    ('drama', 'Drama'),
    ('comedy', 'Comedy'),
    ('sport', 'Sport'),
    ('news', 'News'),
    ('documentary', 'Documentary'),
    ('entertainment', 'Entertainment'),
    ('kids', 'Kids'),
    ('music', 'Music'),
]

class Channel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES)
    country = models.CharField(max_length=100, blank=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('channel_detail', kwargs={'pk': self.pk})
