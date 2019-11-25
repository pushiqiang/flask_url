# -*- coding: utf-8 -*-
from flask import request


def index():
    return "Hello World!"


def upload():
    print(request.method)
    return "Request method: %s" % request.method
