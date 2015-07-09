
from panels import forms


#
#
# from vesper.views import DashboardView
# from vesper.panels import ChartPanel
# from vesper import forms
#
#
# class TurnoverPanel(ChartPanel):
#     title = _('Turnover Panel')
#
#     def get_context(self):
#         return {}
#
#     def render(self):
#         pass
#
# class DashboardView(object):
#
#     panels = [
#         [TurnoverPanel],
#     ]
#
#
# class ResourceView(object):
#     pass
#
#
# class OfferForm(object):
#     pass


# class OfferView(ResourceView):
#     resource = 'scm/offer'
#
#     form = OfferForm
#
#     def index(self):
#         pass
#
#     def update(self):
#         pass
#
#     def create(self):
#         pass
#
#     def delete(self):
#         pass


# class OfferProductInline(object):
#     form = OfferProductForm
#
#
# class OfferChannelInline(object):
#     form = OfferChannelForm
#
#
# class OfferView(object):
#
#     inlines = [
#         OfferProductInline,
#         OfferChannelInline
#     ]
#
#
#     formset = {
#         'basic': {
#             'title': 'Name Of Fieldset',
#             'fields': [
#                 'field_one',
#                 'field_two',
#                 'field_three',
#             ]
#         },
#         'products': {
#             'inlines': 'OfferProductInline'
#         }
#     }

from django.views.generic.edit import FormView

class DemoForm(forms.Form):

    name = forms.CharField(max_length=100)
    email = forms.EmailField()



class DemoFormView(FormView):
    form_class = DemoForm
    form_layout = forms.Layout(
        forms.Fieldset(
            'DETAILS',
            'name',
            'email',
            forms.FormActions(
                forms.Submit('create', 'Create New Object'),
                forms.Button('cancel', 'Cancel')
            )
        )
    )

    template_name = 'form.html'

    def get_form(self, form_class):
        form_class = super(DemoFormView, self).get_form(form_class)
        form_class.helper.layout = self.form_layout
        form_class.helper.form_class = 'form-horizontal'
        form_class.helper.label_class = 'col-lg-2'
        form_class.helper.field_class = 'col-lg-8'
        return form_class



