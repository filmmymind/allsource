# Generated by Django 3.0 on 2020-01-19 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0023_auto_20200118_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='replytext',
            field=models.TextField(default=None,null=True),
            preserve_default=False,
        ),
    ]
