# Generated by Django 2.2.1 on 2019-05-27 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messages_api', '0008_auto_20190527_0520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(upload_to='users_profile_images'),
        ),
    ]
