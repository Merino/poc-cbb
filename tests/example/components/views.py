from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView


class ComponentButtonView(TemplateView):
    template_name = 'component_button.html'


class ComponentButtonGroupView(TemplateView):
    template_name = 'component_button_group.html'


class ComponentBreadcrumb(TemplateView):
    template_name = 'component_breadcrumb.html'


class ComponentChart(TemplateView):
    template_name = 'component_chart.html'


class ComponentForm(TemplateView):
    template_name = 'component_form.html'


class ComponentLabel(TemplateView):
    template_name = 'component_label.html'