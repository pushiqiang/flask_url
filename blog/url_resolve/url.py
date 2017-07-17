# -*- coding: utf-8 -*-

import os
from importlib import import_module


class URLPattern(object):
    def __init__(self, regex, view, kwargs, name):
        self.regex = regex
        self.view = view
        self.kwargs = kwargs
        self.name = name


class URLIncludePatterns(object):
    def __init__(self, urlconf_module):
        self.patterns = []
        if isinstance(urlconf_module, basestring):
            urlconf_module = import_module(urlconf_module)

        self.patterns = getattr(urlconf_module, 'urlpatterns', urlconf_module)
        if not filter(lambda pattern: isinstance(pattern, URLPattern), self.patterns):
            raise Exception


class RegexURLResolver(object):
    def __init__(self, regex, include, kwargs):
        self.patterns = include.patterns
        for pattern in self.patterns:
            if pattern.regex.startswith('/'):
                pattern.regex = os.path.join(regex, pattern.regex.lstrip('/'))
            else:
                pattern.regex = os.path.join(regex, pattern.regex)


def url(regex, view, kwargs=None, name=None):
    # include
    if isinstance(view, URLIncludePatterns):
        return RegexURLResolver(regex, view, kwargs)
    # url
    elif callable(view):
        return URLPattern(regex, view, kwargs, name)
    # 防守编程
    else:
        raise TypeError('view must be a callable or a list/tuple in the case of include().')


include = URLIncludePatterns


def auto_register_url(app):
    """
    自动注册url映射
    :return:
    """
    urlconf_module = import_module(app.config['ROOT_URLCONF'])
    url_patterns = getattr(urlconf_module, 'urlpatterns')
    for url_pattern in url_patterns:
        if isinstance(url_pattern, URLPattern):
            app.add_url_rule(
                url_pattern.regex,
                endpoint=url_pattern.name,
                view_func=url_pattern.view
            )
        else:
            for pattern in url_pattern.patterns:
                app.add_url_rule(
                    pattern.regex,
                    endpoint=pattern.name,
                    view_func=pattern.view
                )
