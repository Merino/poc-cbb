from django.contrib import admin
from django.conf.urls import patterns, url
from django.core import urlresolvers


# from vesper.apps import site
# from vesper.views import ModelAdmin
from panels.layouts import Tab, Fieldset, Field, Button, Inline, Layout
from panels.views import ModelAdmin, BaseAdmin, EditAdmin, StackedInlineAdmin, TabularInlineAdmin


from .models import ListData, GlobalA, GlobalB, NestedA, NestedB1, NestedC1
from .forms import CreateShipmentForm, CreatePackageForm


class ExtraViewAdmin(EditAdmin):
    admin = None
    template_name = 'views/extra.html'
    form_class = CreateShipmentForm
    form_layout = Layout(
                Fieldset('Shipment',
                    Field('channel'),
                    Field('shipment_number'),
                    Field('parcels'),
                    Field('reference'),

                )
            )

    inlines = [
        CreatePackageForm
    ]

    def get_form_initial(self):
        """
        """
        initial = {
            'reference': self.object.name,
        }

        return initial

    def get_form_kwargs(self):
        """
        """
        kwargs = {
            'choices_channel': [(1, 'Channel 1'), (2, 'Channel 2')],
            'choices_shipment_method': [(2, 'Shipment Method A'), (100, 'Shipment Method B')]
        }

        return kwargs

    def form_valid(self, form):
        """
        """

        return super(ExtraViewAdmin, self).form_valid(form)




class ListDataAdmin(ModelAdmin):



    detail_layout = [
        Tab('General',
            Fieldset('Name',
                Field('name'),
                Field('date'),
            ),
            Fieldset('Status',
                Field('boolean'),
                Field('select'),
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


class NestedC1InlineAdmin(TabularInlineAdmin):
    model = NestedC1

class NestedB1InlineAdmin(TabularInlineAdmin):
    model = NestedB1

    inlines = [
        NestedC1InlineAdmin
    ]



class NestedAAdmin(ModelAdmin):

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