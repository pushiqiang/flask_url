# -*- coding: utf-8 -*-

from url_resolvers.resolvers import url, include

from .views import index


urlpatterns = [
    url('index/', index, name='index'),
]
