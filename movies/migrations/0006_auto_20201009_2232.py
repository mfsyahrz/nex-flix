# Generated by Django 3.1.2 on 2020-10-09 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_remove_movies_genre_ids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='title',
            field=models.TextField(),
        ),
    ]
