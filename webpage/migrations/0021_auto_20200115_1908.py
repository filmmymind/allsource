# Generated by Django 3.0 on 2020-01-15 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0020_auto_20200114_0041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewmovie',
            name='image_width',
        ),
        migrations.AlterField(
            model_name='reviewmovie',
            name='image_height',
            field=models.PositiveIntegerField(blank=True, default='300', editable=False, null=True),
        ),
    ]
