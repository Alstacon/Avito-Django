# Generated by Django 4.1.3 on 2022-11-11 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0008_remove_user_location_alter_ad_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='images/'),
        ),
    ]