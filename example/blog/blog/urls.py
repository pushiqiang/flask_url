# -*- coding: utf-8 -*-

from url_resolvers import url, include

from views import home


urlpatterns = [
    url('/home/', home),
    url('/post/', include('post.urls')),
]
