# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-13 23:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0003_auto_20180713_2316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='book_authors',
        ),
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='authors', to='book_authors.Book'),
        ),
    ]
