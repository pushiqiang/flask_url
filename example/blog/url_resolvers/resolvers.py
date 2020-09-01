# -*- coding: utf-8 -*-

from importlib import import_module
from urllib.parse import urljoin

from exceptions import ImproperlyConfigured


class Router:
    def __init__(self, rule, view, name=None, **kwargs):
        self.rule = rule
        self.view = view
        self.name = name
        self.kwargs = kwargs


class URLInclude:
    def __init__(self, urlconf_module):
        self.patterns = []
        if isinstance(urlconf_module, str):
            try:
                urlconf_module = import_module(urlconf_module)
            except ImportError:
                raise ImproperlyConfigured('Urls is not configured correctly')

        self.patterns = getattr(urlconf_module, 'urlpatterns')


class URLNode:
    def __init__(self, route, view, name, **kwargs):
        self.route = route
        self.view = view
        self.kwargs = kwargs
        self.name = name


class URLResolver:
    def __init__(self, url_patterns):
        self.url_patterns = url_patterns
        self.routers = []

    def join_route(self, base_route, route):
        base_route = base_route.rstrip('^')
        if not base_route.endswith('/'):
            base_route = '{}/'.format(base_route)

        route = route.lstrip('^').lstrip('/')

        return urljoin(base_route.rstrip('^'), route)

    def _resolve(self, route, pattern):
        new_route = self.join_route(route, pattern.route)
        if callable(pattern.view):
            self.routers.append(Router(new_route, pattern.view, pattern.name))
        elif isinstance(pattern.view, URLInclude):
            for _pattern in pattern.view.patterns:
                self._resolve(new_route, _pattern)

    def resolve(self):
        for _pattern in self.url_patterns:
            self._resolve('', _pattern)
        return self.routers


def url(route, view, name=None, **kwargs):
    if isinstance(view, URLInclude) or callable(view):
        return URLNode(route, view, name, **kwargs)
    else:
        raise TypeError('view must be a callable or a URLInclude object in the case of include().')


include = URLInclude


def auto_register_urls(app):
    """
    自动注册url映射
    """
    try:
        urlconf_module = import_module(app.config['ROOT_URLCONF'])
    except (KeyError, ImportError):
        raise ImproperlyConfigured('ROOT_URLCONF is not configured correctly')

    url_patterns = getattr(urlconf_module, 'urlpatterns')
    routers = URLResolver(url_patterns).resolve()

    for router in routers:
        app.add_url_rule(
            router.rule,
            endpoint=router.name,
            view_func=router.view,
            **router.kwargs
        )
