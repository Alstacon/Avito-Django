from django.db import models
from django.db.models import Count


class Location(models.Model):
    name = models.CharField(max_length=50, unique=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)

    class Meta:
        verbose_name = 'Место нахождения'
        verbose_name_plural = 'Места нахождения'

    def __str__(self):
        return self.name


class User(models.Model):
    ROLE = [
        ('Пользователь', 'member'),
        ('Администратор', 'admin'),
        ('Модератор', 'moderator')
    ]

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=25, null=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=15, choices=ROLE, default='member')
    age = models.PositiveSmallIntegerField()
    location = models.ManyToManyField(Location)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']

    def __str__(self):
        return self.username

    @property
    def total_ads(self):
        return self.ads.filter(is_published=True).count()
