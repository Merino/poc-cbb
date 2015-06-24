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


class OfferProductInline(object):
    form = OfferProductForm


class OfferChannelInline(object):
    form = OfferChannelForm


class OfferView(object):

    inlines = [
        OfferProductInline,
        OfferChannelInline
    ]


    formset = {
        'basic': {
            'title': 'Name Of Fieldset',
            'fields': [
                'field_one',
                'field_two',
                'field_three',
            ]
        },
        'products': {
            'inlines': 'OfferProductInline'
        }
    }




