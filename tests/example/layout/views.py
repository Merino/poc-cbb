from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView


class GridTemplateView(TemplateView):
    template_name = 'grid.html'

class BlocksTemplateView(TemplateView):
    template_name = 'blocks.html'


class TypoTemplateView(TemplateView):
    template_name = 'typography.html'


class IconTemplateView(TemplateView):
    template_name = 'icon.html'


class ElementTemplateView(TemplateView):
    template_name = 'element.html'

    # Buttons
    # Panels
    # Models
    # Notification


class FormTemplateView(TemplateView):
    template_name = 'forms.html'


class DashboardView(TemplateView):
    template_name = 'dashboard.html'


