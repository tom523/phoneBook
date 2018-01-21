# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phonebook',
            name='office_num',
        ),
        migrations.AddField(
            model_name='phonebook',
            name='home_num',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AddField(
            model_name='phonebook',
            name='office_phone',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AddField(
            model_name='phonebook',
            name='room_num',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='phonebook',
            name='name',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='phonebook',
            name='phone_num',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='phonebook',
            name='short_num',
            field=models.CharField(default=0, max_length=20),
        ),
    ]
