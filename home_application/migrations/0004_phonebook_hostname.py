# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0003_phonebook_os_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonebook',
            name='hostname',
            field=models.CharField(default=b'default', max_length=20),
        ),
    ]
