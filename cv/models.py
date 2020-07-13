from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

class Card(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('card_detail', args=[str(self.id)])