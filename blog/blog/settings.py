# -*- encoding: utf-8 -*-
"""
配置文件
"""

DEBUG=True

ROOT_URLCONF = 'blog.urls'

SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:root@db/flask?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False
