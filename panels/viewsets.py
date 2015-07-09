# encoding: utf-8

from django.conf.urls import patterns, include
from django.core.urlresolvers import reverse_lazy


class BaseViewSet(object):
    def __init__(self, **kwargs):
        super(BaseViewSet, self).__init__()
        for key, value in kwargs.iteritems():
            assert hasattr(self, key), 'Pass unknown parameter'
            setattr(self, key, value)

    def get_urls(self):
        urls = []
        nested = patterns('', *urls)
        return include(nested)

    def reverse(self, name, *args, **kwargs):
        return reverse_lazy(name, args=args, kwargs=kwargs)

    @property
    def urls(self):
        if not hasattr(self, '_urls'):
            self._urls = self.get_urls()
        return self._urls