# Generated by Django 2.2.1 on 2019-05-28 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('messages_api', '0009_auto_20190527_0525'),
    ]

    operations = [
        migrations.CreateModel(
            name='Replay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('replay_content', models.TextField(blank=True)),
                ('message', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='messages_api.Message')),
            ],
        ),
    ]
