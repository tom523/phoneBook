# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0002_auto_20180121_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonebook',
            name='os_type',
            field=models.CharField(default=b'linux', max_length=20),
        ),
    ]
