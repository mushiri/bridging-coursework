from django.db import models
from django.urls import reverse

class App(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()
    image = models.CharField(max_length=100)

    def __str__(self):
        return self.body[:50]

    def get_absolute_url(self):
        return reverse('app_detail', args=[str(self.id)])