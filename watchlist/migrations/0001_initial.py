# Generated by Django 3.1.2 on 2020-10-10 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('tmdb_id', models.IntegerField()),
                ('status', models.CharField(max_length=20)),
                ('comment', models.TextField()),
            ],
        ),
    ]
