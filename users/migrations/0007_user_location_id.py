# Generated by Django 4.1.3 on 2022-11-10 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_user_location_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='location_id',
            field=models.ManyToManyField(to='users.location'),
        ),
    ]
