# Generated by Django 4.2.5 on 2023-09-30 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_list', '0003_reviews_reviewer'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='movie',
            name='number_of_ratings',
            field=models.IntegerField(default=0),
        ),
    ]
