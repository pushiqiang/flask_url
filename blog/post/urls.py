# -*- coding: utf-8 -*-

from url_resolvers.resolvers import url, include

from .views import index, upload


urlpatterns = [
    url('index/', index, name='index'),
    url('upload/', upload, name='upload', methods=['POST']),
]
