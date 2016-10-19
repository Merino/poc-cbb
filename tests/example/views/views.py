# from django.forms import ModelForm
# from django.forms.formsets import formset_factory
# from django.contrib import admin
# from django.utils.translation import ugettext_lazy as _
#
# from datetime import date
# from django.db.models import Count, Q
#
# # from django.views.generic.base import View, TemplateView
# # # Create your views here.
# #
# # from .models import NestedA, NestedB
# #
# #
# # class NestedAForm(ModelForm):
# #     class Meta:
# #         model = NestedA
# #
# #
# # class NestedBForm(ModelForm):
# #     class Meta:
# #         model = NestedB
# #
# #
# # class SingleFormView(CreateView):
# #     form_class = NestedAForm
# #     template_name = 'form_single.html'
# #     success_url = '/views/form/single/'
# #
# #
# # class BaseInline(object):
# #     form_class = None
# #
# #     def get_inline_formsets(self):
# #         return formset_factory(self.form_class)
# #
# # class NestedBInline(BaseInline):
# #     form_class = NestedBForm
#
# from panels.views.data import ListView, UpdateView, CreateView, DeleteView
# from panels.views.base import ModelViewSet
# from .models import ListData, NestedA
#
# from django.utils.encoding import force_text
# from django.utils.http import urlencode
#
#
# class DecadeBornListFilter(admin.SimpleListFilter):
#     # Human-readable title which will be displayed in the
#     # right admin sidebar just above the filter options.
#     title = _('decade born')
#
#     # Parameter for the filter that will be used in the URL query.
#     parameter_name = 'decade'
#
#     def __init__(self, request, params, model, model_admin):
#         super(DecadeBornListFilter, self).__init__(request, params, model, model_admin)
#
#         self.params = dict(request.GET.items())
#
#     def get_query_string(self, new_params=None, remove=None):
#         if new_params is None:
#             new_params = {}
#         if remove is None:
#             remove = []
#         p = self.params.copy()
#         for r in remove:
#             for k in list(p):
#                 if k.startswith(r):
#                     del p[k]
#         for k, v in new_params.items():
#             if v is None:
#                 if k in p:
#                     del p[k]
#             else:
#                 p[k] = v
#         return '?%s' % urlencode(sorted(p.items()))
#
#     def lookups(self, request, model_admin):
#         """
#         Returns a list of tuples. The first element in each
#         tuple is the coded value for the option that will
#         appear in the URL query. The second element is the
#         human-readable name for the option that will appear
#         in the right sidebar.
#         """
#         return (
#             ('80s', _('in the eighties')),
#             ('90s', _('in the nineties')),
#         )
#
#     def queryset(self, request, queryset):
#         """
#         Returns the filtered queryset based on the value
#         provided in the query string and retrievable via
#         `self.value()`.
#         """
#         # Compare the requested value (either '80s' or '90s')
#         # to decide how to filter the queryset.
#         if self.value() == '80s':
#             return queryset.filter(birthday__gte=date(1980, 1, 1),
#                                     birthday__lte=date(1989, 12, 31))
#         if self.value() == '90s':
#             return queryset.filter(birthday__gte=date(1990, 1, 1),
#                                     birthday__lte=date(1999, 12, 31))
#
#     def choices(self):
#         yield {
#             'selected': self.value() is None,
#             'query_string': self.get_query_string({}, [self.parameter_name]),
#             'display': _('All'),
#         }
#         for lookup, title in self.lookup_choices:
#             yield {
#                 'selected': self.value() == force_text(lookup),
#                 'query_string': self.get_query_string({
#                     self.parameter_name: lookup,
#                 }, []),
#                 'display': title,
#             }
#
#
# class BooleanListFilter(admin.SimpleListFilter):
#     # Human-readable title which will be displayed in the
#     # right admin sidebar just above the filter options.
#     title = _('Decimal')
#
#     # Parameter for the filter that will be used in the URL query.
#     parameter_name = 'decimal'
#
#     def __init__(self, request, params, model, model_admin):
#         super(BooleanListFilter, self).__init__(request, params, model, model_admin)
#         self.params = dict(request.GET.items())
#
#     def get_query_string(self, new_params=None, remove=None):
#         if new_params is None:
#             new_params = {}
#         if remove is None:
#             remove = []
#         p = self.params.copy()
#         for r in remove:
#             for k in list(p):
#                 if k.startswith(r):
#                     del p[k]
#         for k, v in new_params.items():
#             if v is None:
#                 if k in p:
#                     del p[k]
#             else:
#                 p[k] = v
#         return '?%s' % urlencode(sorted(p.items()))
#
#     def lookups(self, request, view):
#         """
#         Returns a list of tuples. The first element in each
#         tuple is the coded value for the option that will
#         appear in the URL query. The second element is the
#         human-readable name for the option that will appear
#         in the right sidebar.
#         """
#
#         qs = view.get_queryset()
#         qs = qs.values('decimal').annotate(count=Count("pk")).order_by('decimal')
#
#         for obj in qs:
#             yield (str(obj['decimal']), '%s (%s)' % (obj['decimal'], obj['count']))
#
#     def queryset(self, request, queryset):
#         """
#         Returns the filtered queryset based on the value
#         provided in the query string and retrievable via
#         `self.value()`.
#         """
#         # Compare the requested value (either '80s' or '90s')
#         # to decide how to filter the queryset.
#         if self.value():
#             return queryset.filter(decimal=self.value())
#
#     def choices(self):
#         yield {
#             'selected': self.value() is None,
#             'query_string': self.get_query_string({}, [self.parameter_name]),
#             'display': _('All'),
#         }
#         for lookup, title in self.lookup_choices:
#             yield {
#                 'selected': self.value() == force_text(lookup),
#                 'query_string': self.get_query_string({
#                     self.parameter_name: lookup,
#                 }, []),
#                 'display': title,
#             }
#
#
# class ListDataModelView(ModelViewSet):
#     model = ListData
#     name = 'listdata'
#     app_name = 'views'
#
#     list_display = [
#         'name',
#         'date',
#         'datetime',
#         'boolean',
#         'decimal'
#     ]
#
#     list_filter = [
#         DecadeBornListFilter,
#         BooleanListFilter
#     ]
#
# # class ListDataView(ListView):
# #     queryset = ListData.objects.all()
# #
# #     list_display = [
# #         'name',
# #         'date',
# #         'datetime',
# #         'boolean',
# #         'decimal'
# #     ]
# #
# #     list_search = []
# #     list_facets = []
# #     list_actions = []
# #     list_ordering = []
# #
# #     detail_actions = []
# #     detail_layout = []
# #     detail_inlines = []
# #
# #     def get_context_data(self, **kwargs):
# #         list_headers = self.list_display
# #
# #         for object in self.get_queryset():
# #             print object
# #
# #         list_results = [
# #             1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# #         ]
# #
# #         return {'list_headers': list_headers, 'list_results': list_results}
#
#
# class ListUpdateDataView(UpdateView):
#     model = ListData
#
#     success_url = '/success/'
#
#     template_name = 'object_update.html'
#
#     fields = [
#         'name',
#         'date',
#         'datetime',
#         'boolean',
#         'decimal',
#     ]
#
# class ListCreateDataView(CreateView):
#     model = ListData
#
#     success_url = '/success/'
#
#     template_name = 'object_create.html'
#
#     fields = [
#         'name',
#         'date',
#         'datetime',
#         'boolean',
#         'decimal',
#     ]
#
#
# class ListDeleteDateView(DeleteView):
#     model = ListData
#
#     success_url = '/success/'
#     template_name = 'object_delete.html'
#
#
#
