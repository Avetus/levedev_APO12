# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=500)),
                ('date', models.DateTimeField()),
                ('tru', models.BooleanField(default=0)),
                ('rating', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('header', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=500)),
                ('date', models.DateTimeField()),
                ('rating', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=50)),
                ('registration_date', models.DateTimeField()),
                ('rating', models.IntegerField(default=0)),
                ('avatar', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='question',
            name='autor',
            field=models.ForeignKey(to='polls.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(to='polls.Tags'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='autor',
            field=models.ForeignKey(to='polls.User'),
            preserve_default=True,
        ),
    ]
