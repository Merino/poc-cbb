from __future__ import unicode_literals


import json

from django.contrib import admin
from django.conf.urls import patterns, url
from django.core import urlresolvers
from django.template.defaultfilters import capfirst
from django.utils.translation import ugettext, ugettext_lazy as _


# from vesper.apps import site
# from vds.apps import site
# from vesper.views import ModelAdmin

from panels.layouts import Tab, Fieldset, Field, Button, Inline, Layout, FormHelper
from panels.views import ModelAdminView, TabularModelAdminInline, FormAdminView, TabularFormAdminInline, TemplateAdminView


from .models import ListData, GlobalA, GlobalB, NestedA, NestedB1, NestedC1
from .forms import CreateShipmentForm, CreatePackageForm, FieldsForm



class PageAdminView(TemplateAdminView):
    admin = None
    template_name = 'views/base.html'


class CreatePackageInline(TabularFormAdminInline):
    """
    """
    name = 'packages'

    form_class = CreatePackageForm
    form_layout = Layout(
        Field('length'),
        Field('width'),
        Field('height'),
        Field('weight')
    )


class ExtraViewAdmin(FormAdminView):
    """
    """
    form_class = CreateShipmentForm
    form_layout = Layout(
                    Fieldset('Fields',
                        Field('channel'),
                        Field('shipment_method'),
                        Field('shipment_number'),
                        Field('parcels'),
                        Field('reference'),
                        Field('print_labels')
                    ),
                    Fieldset('Extra',
                        Inline('packages'),
                        css_id='fieldset-extra'
                    )
                  )

    inlines = [
        CreatePackageInline
    ]

    def get_form_initial(self):
        """
        """
        initial = {
            'reference': self.object.name,
        }
        return initial

    def get_form_kwargs(self, **kwargs):
        """
        """
        kwargs = super(ExtraViewAdmin, self).get_form_kwargs()
        kwargs.update({
            'choices_channel': [(1, 'Channel 1'), (2, 'Channel 2')],
            'choices_shipment_method': [(2, 'Shipment Method A'), (100, 'Shipment Method B')]
        })

        return kwargs

    def form_valid(self, form):
        """
        """
        print form.cleaned_data
        return self.form_invalid(form=form)





class ListDataAdmin(ModelAdminView):



    detail_layout = [
        Tab('General',
            Fieldset('Name',
                Field('name'),
                Field('date'),
                    css_class='vds-size--1-of-2'
            ),
            Fieldset('Status',
                Field('boolean'),
                Field('select'),
                    css_class='vds-size--1-of-2'
            )
        ),
        Tab('Info',
            Fieldset('Time',
                Field('datetime'),
                Field('decimal'),
                Field('description'),
            ),
        ),
    ]

    views = [
        url(r'page/$', PageAdminView, name='page'),
        url(r'^(.+)/action/create-shipment/$', ExtraViewAdmin, name='action_shipment'),
    ]

    def get_detail_actions(self, request, obj):
        actions = []

        if obj:
            actions.append(
                Button('create-shipment', 'Markt as Payt', self.get_url_reverse('action_shipment', obj.pk), icon='envelope')
            )

        return actions

    # def get_detail_header(self, request, obj):
    #     header = super(ListDataAdmin, self).get_detail_header(request, obj)
    #     if obj:
    #         header.title = obj.pk
    #         header.subtitle = 'WeStockLots - Website'
    #         header.title = 'WO20180012002'
    #     header.icon = 'pro'
    #     return header


class NestedC1InlineAdmin(TabularModelAdminInline):
    model = NestedC1

class NestedB1InlineAdmin(TabularModelAdminInline):
    model = NestedB1

    inlines = [
        NestedC1InlineAdmin
    ]



class NestedAAdmin(ModelAdminView):

    inlines = [
        NestedB1InlineAdmin
    ]

    detail_layout = [
        Tab('General',
             Fieldset('Name',
                Field('name'),
                Field('global_a'),
                Field('decimal'),
                Field('boolean'),
            ),
            Fieldset('Inline',
                Inline('NestedB1InlineAdmin')
            )
        )
    ]


# Field Test
admin.site.register(ListData, ListDataAdmin)

# Relation Test
admin.site.register(GlobalA)
admin.site.register(GlobalB)
admin.site.register(NestedA, NestedAAdmin)