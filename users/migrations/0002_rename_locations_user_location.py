# Generated by Django 4.1.3 on 2022-11-10 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='locations',
            new_name='location',
        ),
    ]
