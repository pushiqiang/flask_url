# -*- coding: utf-8 -*-
from flask import request
from flask.views import MethodView


def index():
    return "Hello World!"


def upload():
    print(request.method)
    return "Request method: %s" % request.method


class PostListView(MethodView):
    def get(self, *args, **kwargs):
        return "Request GET method"

    def post(self, *args, **kwargs):
        return "Request POST method"

    def patch(self, *args, **kwargs):
        return "Request PATCH method"
