from django.conf.urls import patterns, url

from .data import ListView, UpdateView, CreateView, DeleteView


class ViewSet(object):
    name = None
    routes = []

    def get_urls(self):
        pattern_list = []

        for route in self.routes:
            get_kwargs = getattr(self, "get_%s_kwargs" % route[2], None)

            if not get_kwargs:
                get_kwargs = {}
            else:
                get_kwargs = get_kwargs()

            view_instance = route[1].as_view(**get_kwargs)
            pattern_list.append(
                url(
                    regex=route[0],
                    view=view_instance,
                    name=self.get_view_name(route[2])
                )
            )
        return patterns('', *pattern_list)

    @property
    def urls(self):
        return self.get_urls()

    def get_view_name(self, view_name):
        return '{}_{}'.format(self.name, view_name)


class ModelViewSet(ViewSet):
    model = None

    view_list = ListView
    view_create = CreateView
    view_update = UpdateView
    view_delete = DeleteView

    list_display = []
    list_search = []
    list_facets = []
    list_actions = []
    list_ordering = []
    list_empty_note = 'Please add a new Model to you table'

    detail_actions = []
    detail_layout = []
    detail_inlines = []

    def __init__(self):
        self.routes = [
            [r'^$', self.view_list, 'list'],
            [r'^create/$', self.view_create, 'create'],
            [r'^(?P<pk>\w+)/update/$', self.view_update, 'update'],
            [r'^(?P<pk>\w+)/delete/$', self.view_delete, 'delete'],
        ]

    def get_default_kwargs(self):
        return {
            'model': self.model,
        }

    def get_list_kwargs(self):
        kwargs = self.get_default_kwargs()
        kwargs.update({
            'list_display': self.list_display,
            'list_actions': self.list_actions,
            'list_facets': self.list_facets,
            'list_search': self.list_search,
            'list_ordering': self.list_ordering,
            'list_empty_note': self.list_empty_note
        })
        return kwargs

    def get_create_kwargs(self):
        kwargs = self.get_default_kwargs()
        kwargs.update({
            'detail_layout': self.list_actions,
            'detail_inlines': self.list_facets,
        })
        return kwargs

    def get_update_kwargs(self):
        kwargs = self.get_default_kwargs()
        kwargs.update({
            'detail_actions': self.list_display,
            'detail_layout': self.list_actions,
            'detail_inlines': self.list_facets,
        })
        return kwargs

    def get_delete_kwargs(self):
        return self.get_default_kwargs()