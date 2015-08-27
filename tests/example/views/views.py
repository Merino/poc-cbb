from django.forms import ModelForm
from django.forms.formsets import formset_factory
# from django.views.generic.base import View, TemplateView
# # Create your views here.
#
# from .models import NestedA, NestedB
#
#
# class NestedAForm(ModelForm):
#     class Meta:
#         model = NestedA
#
#
# class NestedBForm(ModelForm):
#     class Meta:
#         model = NestedB
#
#
# class SingleFormView(CreateView):
#     form_class = NestedAForm
#     template_name = 'form_single.html'
#     success_url = '/views/form/single/'
#
#
# class BaseInline(object):
#     form_class = None
#
#     def get_inline_formsets(self):
#         return formset_factory(self.form_class)
#
# class NestedBInline(BaseInline):
#     form_class = NestedBForm

from panels.views.data import ListView, UpdateView, CreateView, DeleteView
from panels.views.base import ModelViewSet
from .models import ListData, NestedA


class ListDataModelView(ModelViewSet):
    model = ListData
    name = 'listdata'
    app_name = 'views'

    list_display = [
        'name',
        'date',
        'datetime',
        'boolean',
        'decimal'
    ]

# class ListDataView(ListView):
#     queryset = ListData.objects.all()
#
#     list_display = [
#         'name',
#         'date',
#         'datetime',
#         'boolean',
#         'decimal'
#     ]
#
#     list_search = []
#     list_facets = []
#     list_actions = []
#     list_ordering = []
#
#     detail_actions = []
#     detail_layout = []
#     detail_inlines = []
#
#     def get_context_data(self, **kwargs):
#         list_headers = self.list_display
#
#         for object in self.get_queryset():
#             print object
#
#         list_results = [
#             1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#         ]
#
#         return {'list_headers': list_headers, 'list_results': list_results}


class ListUpdateDataView(UpdateView):
    model = ListData

    success_url = '/success/'

    template_name = 'object_update.html'

    fields = [
        'name',
        'date',
        'datetime',
        'boolean',
        'decimal',
    ]

class ListCreateDataView(CreateView):
    model = ListData

    success_url = '/success/'

    template_name = 'object_create.html'

    fields = [
        'name',
        'date',
        'datetime',
        'boolean',
        'decimal',
    ]


class ListDeleteDateView(DeleteView):
    model = ListData

    success_url = '/success/'
    template_name = 'object_delete.html'



