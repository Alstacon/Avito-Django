# Generated by Django 4.1.3 on 2022-11-30 11:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator('(^(\\d?|[a-zа-я]?|[A-ZА-Я]?|[?=.*]?){6,}$')]),
        ),
    ]
