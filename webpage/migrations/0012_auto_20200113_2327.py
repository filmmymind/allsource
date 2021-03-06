# Generated by Django 3.0 on 2020-01-13 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0011_auto_20200113_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewmovie',
            name='actor',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='reviewmovie',
            name='director',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='reviewmovie',
            name='movie_image',
            field=models.ImageField(upload_to='movie_image'),
        ),
        migrations.AlterField(
            model_name='reviewmovie',
            name='score',
            field=models.FloatField(),
        ),
    ]
