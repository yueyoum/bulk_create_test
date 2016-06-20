#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:        Wang Chao <yueyoum@gmail.com>
Filename:      set_random_data.py
Date created:  2016-06-20 17:45:27
Description:

"""

import os
import sys
import uuid
import random
import pymysql

pymysql.install_as_MySQLdb()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mytest1.settings")

import django
django.setup()

from myapp.models import TestModel

try:
    AMOUNT = int(sys.argv[1])
except:
    AMOUNT = 10000

def create_random_data():
    data = []
    for i in range(1, AMOUNT+1):
        data.append({
            'id': i,
            'f1': str(uuid.uuid4()),
            'f2': random.randint(1, 10000),
            'f3': str(uuid.uuid4()),
            'f4': random.randint(1, 10000),
            })

    return data

def set_data():
    TestModel.objects.all().delete()

    data = create_random_data()
    objs = [TestModel(**d) for d in data]

    TestModel.objects.bulk_create(objs)

if __name__ == '__main__':
    set_data()
