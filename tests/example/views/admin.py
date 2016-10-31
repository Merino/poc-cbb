from django.contrib import admin
from django.conf.urls import patterns, url
from django.core import urlresolvers


# from vesper.apps import site
# from vesper.views import ModelAdmin
from panels.layouts import Tab, Fieldset, Field, Button, Inline, Layout, FormHelper
from panels.views import ModelAdmin, BaseAdmin, EditAdmin, StackedInlineAdmin, TabularInlineAdmin


from .models import ListData, GlobalA, GlobalB, NestedA, NestedB1, NestedC1
from .forms import CreateShipmentForm, CreatePackageForm

from django.forms import formset_factory


class FormsetView(object):
    """
        Base Inline form view
    """
    name = None
    template_name = 'vds/forms/inline/base.html'
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
        return [
            {'packages': ''}
        ]

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
        formset_instance.helper = FormHelper()
        formset_instance.helper.form_tag = False
        formset_instance.helper.layout = self.get_formset_layout()
        formset_instance.helper.template_pack = 'vds/forms'

        return formset_instance

    def get_formset_layout(self):
        """
        """
        return self.form_layout



class CreatePackageInline(FormsetView):
    name = 'packages'

    form_class = CreatePackageForm
    from_layout = Layout(
        Field('length'),
        Field('width')
    )


class ExtraViewAdmin(EditAdmin):
    admin = None
    template_name = 'views/extra.html'
    form_class = CreateShipmentForm
    form_layout =   Layout(
                        Fieldset('Shipment',
                            Field('channel'),
                            Field('shipment_number'),
                            Field('parcels'),
                            Field('reference'),
                            Field('shipment_method'),
                        ),
                        Fieldset('Packages',
                            Inline('packages')
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

        return super(ExtraViewAdmin, self).form_valid(form=form)


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