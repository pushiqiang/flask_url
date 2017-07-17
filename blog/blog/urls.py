# -*- coding: utf-8 -*-

from url_resolve.url import url, include


urlpatterns = [
    url('/post/', include('post.urls')),
]
