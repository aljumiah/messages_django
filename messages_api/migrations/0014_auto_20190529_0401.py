# Generated by Django 2.2.1 on 2019-05-29 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messages_api', '0013_auto_20190529_0345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.TextField(),
        ),
    ]
