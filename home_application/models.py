# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""

from django.db import models


class PhoneBook(models.Model):
    name = models.CharField(max_length=20, default=0)
    home_num = models.CharField(max_length=20, default=0)
    phone_num = models.CharField(max_length=20, default=0)
    short_num = models.CharField(max_length=20, default=0)
    office_phone = models.CharField(max_length=20, default=0)
    room_num = models.CharField(max_length=20, default=0)
    os_type = models.CharField(max_length=20, default='linux')
    hostname = models.CharField(max_length=20, default='default')

    def __str__(self):
        return self.name + " " + self.os_type + " " + self.hostname


class HostInfo(models.Model):
    os_type = models.CharField(max_length=20, default='linux')
    hostname = models.CharField(max_length=20, default='default')
    ip = models.CharField(max_length=20, default=0)

    def __str__(self):
        return self.os_type + " " + self.hostname + " " + self.ip


