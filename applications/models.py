from django.db import models
from django.urls import reverse

class App(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    description = models.TextField()
    image_main = models.CharField(max_length=100)
    image_detail = models.CharField(max_length=100)

    def __str__(self):
        return self.description[:50]

    def get_absolute_url(self):
        return reverse('app_detail', args=[str(self.id)])