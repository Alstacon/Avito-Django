import re

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from users.validators import age_validator


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

    role = models.CharField(max_length=20, choices=ROLE, default='member')
    age = models.PositiveSmallIntegerField(null=True)
    location = models.ManyToManyField(Location)
    birth_date = models.DateField(validators=[age_validator], null=True)
    email = models.EmailField(max_length=50, unique=True, null=True)
    password = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']

    def __str__(self):
        return self.username


