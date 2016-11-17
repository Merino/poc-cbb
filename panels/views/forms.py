import json

from django.contrib import admin
from django.core import urlresolvers
from django.conf.urls import url
from django.db import models
from django.http import HttpResponseRedirect
from django.forms import formset_factory
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.template import Context

from django.contrib import admin
from django.conf.urls import patterns, url
from django.core import urlresolvers
from django.template.defaultfilters import capfirst
from django.utils.translation import ugettext, ugettext_lazy as _

from ..layouts import FormHelper, Layout, TabHolder, Tab, Fieldset, Field, Button
from ..widgets import ForeignKeyWidget, InputWidget


import nested_admin

#from .models import Product, Category, CategoryItem, Author, Genre, Book, Chapter, Section

# from vesper.apps import site
# from vesper.views import ModelAdmin
# from vesper.layouts import Tab, FieldSet, Field

# Register your models here.


class BaseFormAdminInline(object):
    """
        Base Inline form view
    """
    name = None
    template_name = 'vds/forms/inlines/tabular.html'
    form_class = None
    form_layout = None
    extra = 1

    can_order = False
    can_delete = False

    def __init__(self, request):
        """
        """
        self.request = request

    def get_formset_kwarg(self, **kwargs):
        """
        """

        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })

        return kwargs

    def get_formset_initial(self):
        """
        """
        return {}

    def get_formset_class(self):
        """
        """
        formset_class = formset_factory(
                    form=self.form_class,
                    extra=self.extra,
        )

        return formset_class

    def get_formset(self, **kwargs):
        """
        """
        kwargs = self.get_formset_kwarg()
        kwargs['initial'] = self.get_formset_initial()
        kwargs['prefix'] = self.name

        formset_class = self.get_formset_class()
        formset_instance = formset_class(**kwargs)

        # Layout
        formset_instance.helper = FormHelper()
        formset_instance.helper.form_tag = False
        formset_instance.helper.layout = self.get_formset_layout()
        formset_instance.helper.template_pack = 'vds/forms'
        formset_instance.helper.template = self.template_name

        # Data
        formset_instance.data_inline_formset = self.get_formset_data()

        return formset_instance

    def get_formset_layout(self):
        """
        """
        return self.form_layout

    def get_formset_data(self):
        return json.dumps({
            'name': '#%s' % self.name,
            'options': {
                'prefix': self.name,
                'addText': ugettext('Add another %(verbose_name)s') % {
                    'verbose_name': capfirst(self.name),
                },
                'deleteText': ugettext('Remove'),
            }
        })


class TabularFormAdminInline(BaseFormAdminInline):
    """
    """
    pass



class FormAdminView(FormView):
    """
    """
    template_name = 'vds/forms/object_edit.html'

    inlines = []
    admin = None

    form_layout = None

    def __init__(self, **kwargs):
        super(FormAdminView, self).__init__(**kwargs)
        self.model = self.admin.model

    def get_form_layout(self):
        """
        """
        return self.form_layout

    def get_form(self, form_class=None):
        """
        Returns an instance of the form to be used in this view.
        """
        if form_class is None:
            form_class = self.get_form_class()
        form = form_class(**self.get_form_kwargs())

        #form = super(EditAdmin, self).get_form()

        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.layout = self.get_form_layout()
        form.helper.template_pack = 'vds/forms'

        return form

    def get_inlines(self):
        """
        """
        inlines = []

        if self.inlines:
            for inline in self.inlines:
                instance = inline(request=self.request)
                inlines.append(instance)

        return inlines

    def get_success_url(self):
        return self.admin.get_url_reverse('change', self.object.pk)

    def get_object(self, request, object_id):
        """
        """
        return self.admin.get_object(request=request, object_id=object_id)

    def get_context_data(self, **kwargs):

        header = self.admin.get_detail_header(request=self.request, obj=self.object)
        header.subtitle = 'Mail Payment'

        buttons = [
            Button(name='submit', value='Submit', link='submit', style='primary'),
            Button(name='submit', value='Submit', link='submit', style='brand'),
        ]

        context = {
            'detail_header': header,
            'detail_actions': self._render_buttons(buttons),
            'object': self.object,
        }

        kwargs.update(context)

        context = super(FormAdminView, self).get_context_data(**kwargs)

        inlines = self.get_inlines()

        context.update({
            'inline_formsets': inlines
        })

        return context

    def get(self, request, *args, **kwargs):
        """
        """

        self.object = self.get_object(request=request, object_id=args[0])

        context = self.get_context_data()

        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        """
        """
        self.object = self.get_object(request=request, object_id=args[0])

        form = self.get_form()
        formsets = [inline.get_formset() for inline in self.get_inlines()]

        if form.is_valid() and all([f.is_valid() for f in formsets]):
            for f in formsets:
                form.cleaned_data[f.prefix] = f.cleaned_data

            return self.form_valid(form=form)
        else:
            return self.form_invalid(form=form)

    def _render_buttons(self, buttons):
        render_buttons = []
        for button in buttons:
            render_buttons.append(
                button.render(
                    None,
                    None,
                    Context({})
                )
            )

        return render_buttons