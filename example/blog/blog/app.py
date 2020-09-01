# -*- coding: utf-8 -*-

import os
from flask import Flask

from url_resolvers import auto_register_urls

import settings


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)
app.config.from_object(settings)

# 自动注册urls路径
auto_register_urls(app)


def runserver():
    """启动服务器
    根据启动参数加载配置, 如果没有相应的配置文件直接抛出错误
    """
    app.run(host=app.config['HOST'],
            port=app.config['PORT'],
            debug=app.config['DEBUG'])
