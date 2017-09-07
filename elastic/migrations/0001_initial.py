# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Title')),
                ('description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Description')),
                ('text', models.TextField(null=True, verbose_name='Text')),
                ('rate', models.CharField(choices=[('1', 'Bad'), ('5', 'Good')], max_length=1)),
                ('added_date', models.DateTimeField(auto_now_add=True, verbose_name='Add date')),
                ('published_date', models.DateTimeField(auto_now=True, verbose_name='Published date')),
            ],
        ),
    ]
