# -*- coding: utf-8 -*-

import os
from importlib import import_module

import six
from exceptions import ImproperlyConfigured


class URLPattern(object):
    def __init__(self, regex, view, name, **kwargs):
        self.regex = regex
        self.view = view
        self.kwargs = kwargs
        self.name = name


class URLIncludePatterns(object):
    def __init__(self, urlconf_module):
        self.patterns = []
        if isinstance(urlconf_module, six.string_types):
            try:
                urlconf_module = import_module(urlconf_module)
            except ImportError:
                raise ImproperlyConfigured('Urls is not configured correctly')

        self.patterns = getattr(urlconf_module, 'urlpatterns')
        if filter(lambda pattern: isinstance(pattern, URLIncludePatterns), self.patterns):
            raise ImproperlyConfigured(
                'Using included patterns in an included URLconf is not allowed.')


class RegexURLResolver(object):
    def __init__(self, regex, include, **kwargs):
        self.patterns = include.patterns
        self.regex = regex
        self.kwargs = kwargs
        for pattern in self.patterns:
            if pattern.regex.startswith('/'):
                pattern.regex = os.path.join(regex, pattern.regex.lstrip('/'))
            else:
                pattern.regex = os.path.join(regex, pattern.regex)


def url(regex, view, name=None, **kwargs):
    # include
    if isinstance(view, URLIncludePatterns):
        return RegexURLResolver(regex, view, **kwargs)
    # url
    elif callable(view):
        return URLPattern(regex, view, name, **kwargs)
    else:
        raise TypeError('view must be a callable or a list/tuple in the case of include().')


include = URLIncludePatterns


def auto_register_urls(app):
    """
    自动注册url映射
    """
    try:
        urlconf_module = import_module(app.config['ROOT_URLCONF'])
    except (KeyError, ImportError):
        raise ImproperlyConfigured('ROOT_URLCONF is not configured correctly')

    url_patterns = getattr(urlconf_module, 'urlpatterns')
    for url_pattern in url_patterns:
        if isinstance(url_pattern, URLPattern):
            app.add_url_rule(
                url_pattern.regex,
                endpoint=url_pattern.name,
                view_func=url_pattern.view,
                **url_pattern.kwargs
            )
        else:
            for pattern in url_pattern.patterns:
                app.add_url_rule(
                    pattern.regex,
                    endpoint=pattern.name,
                    view_func=pattern.view,
                    **pattern.kwargs
                )
