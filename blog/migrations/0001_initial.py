# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('litdev_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
                ('en_title', models.CharField(max_length=100, verbose_name='\u82f1\u6587\u6807\u9898')),
                ('img', models.CharField(default=b'/static/img/article/default.jpg', max_length=200)),
                ('tags', models.CharField(help_text='\u7528\u9017\u53f7\u5206\u9694', max_length=200, null=True, verbose_name='\u6807\u7b7e', blank=True)),
                ('summary', models.TextField(verbose_name='\u6458\u8981')),
                ('content', models.TextField(verbose_name='\u6b63\u6587')),
                ('view_times', models.IntegerField(default=0, help_text='\u7528\u6237\u6d4f\u89c8\u6570', verbose_name='\u67e5\u770b\u6570\u91cf')),
                ('zan_times', models.IntegerField(default=0, help_text='\u88ab\u8d5e\u7684\u6570\u91cf', verbose_name='\u8d5e\u7684\u6570\u91cf')),
                ('is_top', models.BooleanField(default=False, verbose_name='\u7f6e\u9876')),
                ('rank', models.IntegerField(default=0, verbose_name='\u6392\u5e8f\u6570\u5b57')),
                ('status', models.IntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(0, '\u6b63\u5e38'), (1, '\u8349\u7a3f'), (2, '\u5220\u9664')])),
                ('pub_time', models.DateTimeField(default=False, verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('author', models.ForeignKey(verbose_name='\u4f5c\u8005', blank=True, to='litdev_auth.LitdevUser', null=True)),
            ],
            options={
                'ordering': ['rank', '-is_top', '-pub_time', '-create_time'],
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
                ('summary', models.TextField(null=True, verbose_name='\u6458\u8981', blank=True)),
                ('img', models.CharField(default=b'/static/img/carousel/default.jpg', max_length=200, verbose_name='\u8f6e\u64ad\u56fe\u7247')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('article', models.ForeignKey(verbose_name='\u6587\u7ae0', to='blog.Article')),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': '\u8f6e\u64ad',
                'verbose_name_plural': '\u8f6e\u64ad',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, verbose_name='\u540d\u79f0')),
                ('rank', models.IntegerField(default=0, verbose_name='\u6392\u5e8f')),
                ('status', models.IntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(0, '\u6b63\u5e38'), (1, '\u8349\u7a3f'), (2, '\u5220\u9664')])),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('parent', models.ForeignKey(default=None, blank=True, to='blog.Category', null=True, verbose_name='\u4e0a\u7ea7\u5206\u7c7b')),
            ],
            options={
                'ordering': ['rank', '-create_time'],
                'verbose_name': '\u5206\u7c7b',
                'verbose_name_plural': '\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, verbose_name='\u4e13\u680f\u5185\u5bb9')),
                ('summary', models.TextField(verbose_name='\u4e13\u680f\u6458\u8981')),
                ('status', models.IntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(0, '\u6b63\u5e38'), (1, '\u8349\u7a3f'), (2, '\u5220\u9664')])),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('article', models.ManyToManyField(to='blog.Article', verbose_name='\u6587\u7ae0')),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': '\u4e13\u680f',
                'verbose_name_plural': '\u4e13\u680f',
            },
        ),
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, verbose_name='\u5bfc\u822a\u6761\u5185\u5bb9')),
                ('url', models.CharField(max_length=200, null=True, verbose_name='\u6307\u5411\u5730\u5740', blank=True)),
                ('status', models.IntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(0, '\u6b63\u5e38'), (1, '\u8349\u7a3f'), (2, '\u5220\u9664')])),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': '\u5bfc\u822a\u6761',
                'verbose_name_plural': '\u5bfc\u822a\u6761',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
                ('summary', models.TextField(verbose_name='\u6458\u8981')),
                ('new_from', models.IntegerField(default=0, verbose_name='\u6765\u6e90', choices=[(0, b'\xe5\x8d\x9a\xe5\xae\xa2\xe5\x9b\xad'), (1, b'CSDN'), (2, b'51CTO')])),
                ('url', models.CharField(max_length=200, verbose_name='\u6e90\u5730\u5740')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('pub_time', models.DateTimeField(default=False, verbose_name='\u53d1\u5e03\u65f6\u95f4')),
            ],
            options={
                'ordering': ['-title'],
                'verbose_name': '\u8d44\u8baf',
                'verbose_name_plural': '\u8d44\u8baf',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(verbose_name='\u5206\u7c7b', to='blog.Category'),
        ),
    ]
