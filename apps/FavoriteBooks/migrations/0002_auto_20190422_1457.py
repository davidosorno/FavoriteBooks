# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-04-22 21:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FavoriteBooks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='userLike',
        ),
        migrations.AddField(
            model_name='book',
            name='userLikes',
            field=models.ManyToManyField(related_name='likesBooks', to='FavoriteBooks.User'),
        ),
    ]
