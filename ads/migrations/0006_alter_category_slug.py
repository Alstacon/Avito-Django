# Generated by Django 4.1.3 on 2022-11-30 09:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0005_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=10, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
    ]
