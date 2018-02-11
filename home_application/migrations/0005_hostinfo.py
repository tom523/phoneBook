# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0004_phonebook_hostname'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('os_type', models.CharField(default=b'linux', max_length=20)),
                ('hostname', models.CharField(default=b'default', max_length=20)),
                ('ip', models.CharField(default=0, max_length=20)),
            ],
        ),
    ]
