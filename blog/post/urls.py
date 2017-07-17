# -*- coding: utf-8 -*-

from url_resolve.url import url, include

from .views import index


urlpatterns = [
    url('index/', index, name='index'),
]
