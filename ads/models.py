from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=500)
    address = models.CharField(max_length=150)
    is_published = models.BooleanField(default=False)


class Category(models.Model):
    name = models.CharField(max_length=40)
