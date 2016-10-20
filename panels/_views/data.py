from django.views.generic.list import ListView as ListViewBase
from django.views.generic.edit import UpdateView as UpdateViewBase, DeleteView as DeleteViewBase, CreateView as CreateViewBase


class ListView(ListViewBase):
    name = None

    list_display = []
    list_search = []
    list_filter = []
    list_actions = []
    list_ordering = []

    list_empty_note = None

    template_name = 'panels/list.html'

    def get_context_data(self, request, **kwargs):
        # there is no request object available in the get_context_data so for now we set te value to none
        # maybe this is a good addition.
        #request = None


        list_filter, is_used, lookup_params, use_distinct = self.get_filters(request)

        list_headers = self.get_list_display(request)
        list_results = self.get_result(request)

        context = {
            'list_actions': self.list_actions,
            'list_filter':  list_filter,
            'list_headers': list_headers,
            'list_results': list_results,
            'list_empty_note': self.list_empty_note,
        }

        return context

    def get_list_display(self, request):
        return self.list_display

    def get_list_filter(self, request):
        return self.list_filter

    def get_list_search(self, request):
        return self.list_search

    def get_list_actions(self, request):
        return self.list_actions

    def get_filters_params(self, request, params=None):
        """
        Returns all params except IGNORED_PARAMS
        """
        if not params:
            params = dict(request.GET.items())
        lookup_params = params.copy()  # a dictionary of the query string
        # Remove all the parameters that are globally and systematically
        # ignored.
        #for ignored in IGNORED_PARAMS:
        #    if ignored in lookup_params:
        #        del lookup_params[ignored]
        return lookup_params

    def get_filters(self, request):
        lookup_params = self.get_filters_params(request)
        use_distinct = False

        #for key, value in lookup_params.items():
        #    if not self.model_admin.lookup_allowed(key, value):
        #        raise DisallowedModelAdminLookup("Filtering by %s not allowed" % key)

        filter_specs = []
        if self.list_filter:
            for list_filter in self.list_filter:
                if callable(list_filter):
                    # This is simply a custom list filter class.
                    spec = list_filter(request, lookup_params,
                        self.model, self)
                else:
                    # field_path = None
                    # if isinstance(list_filter, (tuple, list)):
                    #     # This is a custom FieldListFilter class for a given field.
                    #     field, field_list_filter_class = list_filter
                    # else:
                    #     # This is simply a field name, so use the default
                    #     # FieldListFilter class that has been registered for
                    #     # the type of the given field.
                    #     field, field_list_filter_class = list_filter, FieldListFilter.create
                    # if not isinstance(field, models.Field):
                    #     field_path = field
                    #     field = get_fields_from_path(self.model, field_path)[-1]
                    # spec = field_list_filter_class(field, request, lookup_params,
                    #     self.model, self.model_admin, field_path=field_path)
                    # # Check if we need to use distinct()
                    # use_distinct = (use_distinct or
                    #                 lookup_needs_distinct(self.lookup_opts,
                    #                                       field_path))
                    pass
                if spec and spec.has_output():
                    filter_specs.append(spec)

        return filter_specs, bool(filter_specs), lookup_params, use_distinct


        # At this point, all the parameters used by the various ListFilters
        # have been removed from lookup_params, which now only contains other
        # parameters passed via the query string. We now loop through the
        # remaining parameters both to ensure that all the parameters are valid
        # fields and to determine if at least one of them needs distinct(). If
        # the lookup parameters aren't real fields, then bail out.
        #try:
        #    for key, value in lookup_params.items():
        #        lookup_params[key] = prepare_lookup_value(key, value)
        #        use_distinct = (use_distinct or
        #                        lookup_needs_distinct(self.lookup_opts, key))
        #    return filter_specs, bool(filter_specs), lookup_params, use_distinct
        #except FieldDoesNotExist as e:
        #    six.reraise(IncorrectLookupParameters, IncorrectLookupParameters(e), sys.exc_info()[2])

    def get_result(self, request):
        """
            Returns the data in a matrix format
        """
        results = []

        # Then, we let every list filter modify the queryset to its liking.
        (self.filter_specs, self.has_filters, remaining_lookup_params,
         filters_use_distinct) = self.get_filters(request)

        qs = self.get_queryset()
        for filter_spec in self.filter_specs:
            new_qs = filter_spec.queryset(request, qs)
            if new_qs is not None:
                qs = new_qs

        for obj in qs:
            row = []
            for field in self.get_list_display(request):
                row.append(getattr(obj, field))
            results.append(row)

        return results


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