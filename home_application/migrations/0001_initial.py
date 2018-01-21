# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneBook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('phone_num', models.CharField(max_length=20)),
                ('short_num', models.CharField(max_length=20)),
                ('office_num', models.CharField(max_length=20)),
            ],
        ),
    ]
