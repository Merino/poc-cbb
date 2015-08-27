from django.views.generic.list import ListView as ListViewBase
from django.views.generic.edit import UpdateView as UpdateViewBase, DeleteView as DeleteViewBase, CreateView as CreateViewBase


class ListView(ListViewBase):
    name = None

    list_display = []
    list_search = []
    list_facets = []
    list_actions = []
    list_ordering = []

    list_empty_note = None

    template_name = 'panels/list.html'

    def get_context_data(self, **kwargs):

        #print kwargs

        list_headers = self.list_display

        #for object in self.get_queryset():
        #    print object

        list_results = [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10
        ]

        context = {
            'list_actions': self.list_actions,
            'list_facets': self.list_facets,
            'list_headers': list_headers,
            'list_results': list_results,
            'list_empty_note': self.list_empty_note,
        }

        return context


class CreateView(CreateViewBase):
    detail_actions = []
    detail_layout = []
    detail_inlines = []

    template_name = 'panels/create.html'

    fields = [
        'name',
        'date',
        'datetime',
        'boolean',
        'decimal',
    ]

class UpdateView(UpdateViewBase):
    detail_actions = []
    detail_layout = []
    detail_inlines = []

    template_name = 'panels/update.html'

    fields = [
        'name',
        'date',
        'datetime',
        'boolean',
        'decimal',
    ]

class DeleteView(DeleteViewBase):
    template_name = 'panels/delete.html'