from django.contrib import admin
from django.conf.urls import patterns, url
from django.core import urlresolvers


# from vesper.apps import site
# from vesper.views import ModelAdmin
from panels.layouts import Tab, Fieldset, Field, Button
from panels.views import ModelAdmin, BaseAdmin, EditAdmin


from .models import ListData


class ExtraViewAdmin(EditAdmin):
    admin = None
    template_name = 'views/extra.html'



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



admin.site.register(ListData, ListDataAdmin)