from django.views.generic.list import ListView as ListViewBase
from django.views.generic.edit import UpdateView as UpdateViewBase, DeleteView as DeleteViewBase, CreateView as CreateViewBase


class ListView(ListViewBase):
    name = None

    list_display = []
    list_search = []
    list_facets = []
    list_actions = []
    list_ordering = []

    template_name = 'panels/list.html'

    def get_context_data(self, **kwargs):
        list_headers = self.list_display

        for object in self.get_queryset():
            print object

        list_results = [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10
        ]

        context = {
            'list_actions': self.list_actions,
            'list_facets': self.list_facets,
            'list_headers': list_headers,
            'list_results': list_results
        }

        return context


class CreateView(CreateViewBase):
    template_name = 'panels/create.html'


class UpdateView(UpdateViewBase):
    template_name = 'panels/update.html'


class DeleteView(DeleteViewBase):
    template_name = 'panels/delete.html'