# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-13 23:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='authors',
            new_name='Author',
        ),
        migrations.RenameModel(
            old_name='books',
            new_name='Book',
        ),
    ]
