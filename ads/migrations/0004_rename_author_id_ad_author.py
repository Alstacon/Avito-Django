# Generated by Django 4.1.3 on 2022-11-10 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_rename_category_id_ad_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ad',
            old_name='author_id',
            new_name='author',
        ),
    ]
