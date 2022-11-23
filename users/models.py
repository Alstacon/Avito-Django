from django.contrib.auth.models import AbstractUser
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


class User(AbstractUser):
    MEMBER = 'Пользователь'
    ADMIN = 'Администратор'
    MODERATOR = 'Модератор'

    ROLE = [
        (MEMBER, 'member'),
        (ADMIN, 'admin'),
        (MODERATOR, 'moderator')
    ]

    role = models.CharField(max_length=15, choices=ROLE, default='member')
    age = models.PositiveSmallIntegerField(null=True)
    location = models.ManyToManyField(Location)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']

    def __str__(self):
        return self.username


