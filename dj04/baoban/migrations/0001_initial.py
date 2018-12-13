# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='minjing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_minjing', models.CharField(max_length=12, verbose_name=b'\xe6\xb0\x91\xe8\xad\xa6\xe5\xa7\x93\xe5\x90\x8d')),
                ('jinghao_minjing', models.CharField(max_length=8, verbose_name=b'\xe8\xad\xa6\xe5\x8f\xb7')),
                ('lingdao_minjing', models.CharField(max_length=1, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe7\x8b\xb1\xe9\x95\xbf', choices=[('1', '\u662f'), ('0', '\u5426')])),
                ('daiban_minjing', models.CharField(max_length=1, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe4\xbb\xa3\xe7\x8f\xad', choices=[('1', '\u662f'), ('0', '\u5426')])),
                ('w5c_minjing', models.CharField(max_length=1, verbose_name=b'\xe4\xba\x94\xe6\x9f\xa5\xe5\x80\xbc\xe7\x8f\xad', choices=[('1', '\u662f'), ('0', '\u5426')])),
            ],
        ),
        migrations.CreateModel(
            name='org',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_org', models.CharField(max_length=32, verbose_name=b'\xe5\x8d\x95\xe4\xbd\x8d')),
                ('code_org', models.CharField(max_length=2, verbose_name=b'\xe5\x8d\x95\xe4\xbd\x8d\xe4\xbb\xa3\xe7\xa0\x81')),
                ('yafan_org', models.CharField(max_length=1, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x8a\xbc\xe7\x8a\xaf', choices=[('1', '\u662f'), ('0', '\u5426')])),
                ('memo_org', models.TextField(verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='zfrenshu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_zfrenshu', models.DateField(auto_now_add=True, verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f')),
                ('shiya_zfrenshu', models.IntegerField(verbose_name=b'\xe5\xae\x9e\xe6\x8a\xbc')),
                ('jiuyi_zfrenshu', models.IntegerField(verbose_name=b'\xe5\xa4\x96\xe5\x87\xba\xe5\xb0\xb1\xe5\x8c\xbb')),
                ('jinbi_zfrenshu', models.IntegerField(verbose_name=b'\xe7\xa6\x81\xe9\x97\xad')),
                ('other_zfrenshu', models.IntegerField(verbose_name=b'\xe5\x85\xb6\xe4\xbb\x96')),
                ('danwei_zfrenshu', models.ForeignKey(verbose_name=b'\xe5\x8d\x95\xe4\xbd\x8d', to='baoban.org')),
            ],
        ),
        migrations.CreateModel(
            name='zhiban',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_zhiban', models.DateField(auto_now_add=True, verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f')),
                ('fangbao_zhiban', models.CharField(max_length=1, verbose_name=b'\xe9\x98\xb2\xe7\x88\x86\xe9\x98\x9f\xe5\x91\x98', choices=[('1', '\u662f'), ('0', '\u5426')])),
                ('yeban_zhiban', models.CharField(max_length=1, verbose_name=b'\xe5\xa4\x9c\xe7\x8f\xad', choices=[('1', '\u662f'), ('0', '\u5426')])),
                ('name_zhiban', models.ManyToManyField(to='baoban.minjing', verbose_name=b'\xe5\x80\xbc\xe7\x8f\xad\xe6\xb0\x91\xe8\xad\xa6')),
            ],
        ),
        migrations.AddField(
            model_name='minjing',
            name='danwei_minjing',
            field=models.ForeignKey(verbose_name=b'\xe5\x8d\x95\xe4\xbd\x8d', to='baoban.org'),
        ),
    ]
