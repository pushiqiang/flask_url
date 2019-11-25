# -*- coding: utf-8 -*-

import os

from flask import Flask

from url_resolvers.resolvers import auto_register_urls

import settings


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)
app.config.from_object(settings)

# 自动注册urls路径
auto_register_urls(app)
