from django.db import models

# Create your models here.

class Article(models.Model):
    URL1 = models.CharField(max_length=1000)
    URL2 = models.CharField(max_length=1000)

