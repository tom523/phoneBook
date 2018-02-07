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

from common.mymako import render_mako_context, render_json
from django.http import HttpResponse
import xlrd
from models import PhoneBook
from django.core import serializers
import json


def import_excel(request):
    if request.method == "POST":
        myFile = request.FILES.get("myfile", None)
        dest = open(myFile.name, 'wb+')
        for chunk in myFile.chunks():
            dest.write(chunk)
        dest.close()
        data = xlrd.open_workbook(myFile.name)
        table = data.sheet_by_index(0)
        PhoneBook.objects.all().delete()
        office_phone = ""
        room_num = ""
        for i in range(table.nrows):
            row_list = table.row_values(i)
            if row_list[0] != u"姓名" \
                    and row_list[0] != u"物联网工程学院（信息安全学院）" \
                    and row_list[0] != u"学生管理办公室" \
                    and row_list[0] != u"实验室管理办公室" \
                    and row_list[0] != u"物联网应用技术教研室" \
                    and row_list[0] != u"软件技术教研室" \
                    and row_list[0] != u"网络技术教研室" \
                    and row_list[0] != u"计算机应用技术教研室" \
                    and row_list[0] != u"信息技术教研室":
                if row_list[4] != "":
                    office_phone = row_list[4]
                    room_num = row_list[5]
                print int(row_list[2])
                print type(row_list[2])
                print row_list[2]
                phone_num = int(row_list[2])
                home_num = row_list[1]
                short_num = row_list[3]
                if str(home_num).strip() != "/" and str(home_num) != "":
                    home_num = int(home_num)
                if str(short_num).strip() != "/":
                    short_num = int(short_num)

                PhoneBook(name=row_list[0].replace(' ', ''), home_num=home_num,
                          phone_num=phone_num, short_num=short_num,
                          office_phone=office_phone, room_num=room_num).save()

    return HttpResponse("test")


def phone_book(request):
    all_record = PhoneBook.objects.all()
    data = serializers.serialize("json", all_record)
    data_json = json.loads(data)
    response_data = []
    for item in data_json:
        response_data.append(item["fields"])
    response_data = {"data": response_data}
    return HttpResponse(json.dumps(response_data))


def get_phone_num(request):
    all_record = PhoneBook.objects.all()
    data = serializers.serialize("json", all_record)
    data_json = json.loads(data)
    response_data = []
    for item in data_json:
        response_data.append(item["fields"])
    response_data = {"data": response_data}
    return render_json(response_data)

def home(request):
    """
    首页
    """
    return render_mako_context(request, '/home_application/home.html')


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')
