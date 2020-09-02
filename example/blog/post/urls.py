# -*- coding: utf-8 -*-

from url_resolvers.resolvers import url, include

from .views import index, upload, PostListView


urlpatterns = [
    url('index/', index, name='index'),
    url('upload/', upload, name='upload', methods=['POST']),
    url('list/', PostListView.as_view('test'), name='list'),
]
