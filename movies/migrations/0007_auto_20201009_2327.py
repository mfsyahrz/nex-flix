# Generated by Django 3.1.2 on 2020-10-09 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_auto_20201009_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='vote_average',
            field=models.DecimalField(decimal_places=2, max_digits=2),
        ),
    ]
