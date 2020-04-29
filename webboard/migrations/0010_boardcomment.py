# Generated by Django 3.0 on 2020-01-20 15:46

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webboard', '0009_auto_20200116_1412'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boardcomment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', ckeditor_uploader.fields.RichTextUploadingField()),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('board', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='webboard.boardpost')),
                ('reply', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='webboard.Boardcomment')),
            ],
        ),
    ]
