from django.db import models

# Create your models here.

class Article(models.Model):
    URL = models.CharField(max_length=1000)

