import copy
import json

from django.contrib import admin
from django.core import urlresolvers
from django.conf.urls import url
from django.db import models
from django.http import HttpResponseRedirect
from django.forms import formset_factory
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from django.contrib import admin
from django.conf.urls import patterns, url
from django.core import urlresolvers
from django.template import Context
from django.template.defaultfilters import capfirst
from django.utils.translation import ugettext, ugettext_lazy as _

from ..layouts import FormHelper, Layout, TabHolder, Tab, Fieldset, Field, Button, Header, Breadcrumb
from ..widgets import ForeignKeyWidget, InputWidget


import nested_admin


class TabularModelAdminInline(nested_admin.NestedTabularInline):
    extra = 0

    template = 'vds/models/inlines/tabular.html'

    formfield_overrides = {
        models.ForeignKey: {'widget': ForeignKeyWidget},
        models.CharField: {'widget': InputWidget},
    }

class StackedModelAdminInline(nested_admin.NestedStackedInline):
    template = 'vds/models/inlines/stacked.html'

    extra = 0

    formfield_overrides = {
        models.ForeignKey: {'widget': ForeignKeyWidget},
        models.CharField: {'widget': InputWidget},
    }

class ModelAdminView(nested_admin.NestedModelAdmin):

    # List View
    list_fields = []
    list_filters = []
    list_actions = []
    list_search = []

    # Detail View
    detail_layout = []
    detail_actions = []

    # Extra Views
    views = []

    # Templates
    change_form_template = 'vds/models/object_edit.html'

    formfield_overrides = {
        models.ForeignKey: {'widget': ForeignKeyWidget},
    }

    #   Views Functions
    # ---------------------
    def get_urls(self):
        urls = super(ModelAdminView, self).get_urls()
        extra_urls = []
        for view in self.views:
            name = '%s_%s_%s' % (self.model._meta.app_label, self.model._meta.model_name, view.name)

            extra_urls.append(
                url(view._regex, view._callback.as_view(admin=self), name=name)
            )

        return extra_urls + urls

    def get_url_reverse(self, name, *args):
        info = self.model._meta.app_label, self.model._meta.model_name, name
        return urlresolvers.reverse('admin:%s_%s_%s' % info, args=args)

    #   List Functions
    # ---------------------

    #   Detail Functions
    # ---------------------
    def get_form_layout(self, request, obj=None, **kwargs):
        """
        """
        layout = Layout(
            TabHolder(
                *self.detail_layout
            )
        )
        return layout

    def get_form(self, request, obj=None, **kwargs):
        """
        """
        form = super(ModelAdminView, self).get_form(request, obj, **kwargs)

        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.layout = self.get_form_layout(request, obj, **kwargs)
        form.helper.template_pack = 'vds/forms'

        return form

    def get_detail_title(self, request, obj=None, **kwargs):
        """
        """
        if obj:
            return str(obj)
        else:
            return 'Add %s' % self.model._meta

    def get_detail_navigation(self, request, obj=None, **kwargs):
        """
        """
        navigation = []
        navigation.append(Breadcrumb(title='Dashboard', href='/views/'))
        navigation.append(Breadcrumb(title='App', href='/views/views/'))

        if obj:
            navigation.append(Breadcrumb(title='Model', href='/views/views/listdata/'))

        return navigation

    def get_detail_actions(self, request, obj=None, **kwargs):
        """
        """
        return self.detail_actions

    def _get_detail_action(self, request, obj=None, **kwargs):
        """
            Wrapper function around 'get_detail_actions' to control the form.
        """
        actions = []

        url_index = self.get_url_reverse('changelist')


        if obj:
            url_delete = self.get_url_reverse('delete', obj.pk)
            actions.append(
                Button('delete', 'Delete', url_delete, 'danger', icon='trash')
            )

        actions.append(
            Button('cancel', 'Back', url_index, icon='close')
        )

        actions += copy.copy(self.get_detail_actions(request=request, obj=obj))
        actions.append(
            Button('_continue', 'Save', 'submit', 'primary', icon='save')
        )

        return actions

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        # Object
        obj = self.get_object(request=request, object_id=object_id)

        # Header
        header = Header()
        header.title = self.get_detail_title(request=request, obj=obj)
        header.navigation = self.get_detail_navigation(request=request, obj=obj)
        header.actions = self._get_detail_action(request=request, obj=obj)

        extra_context = {
            'header': header
        }

        response = super(ModelAdminView, self).changeform_view(
                                                request=request,
                                                object_id=object_id,
                                                form_url='',
                                                extra_context=extra_context
                                            )
        return response