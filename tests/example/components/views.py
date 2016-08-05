from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView


class ComponentIndexView(TemplateView):
    template_name = 'component_index.html'

class ComponentMessagesView(TemplateView):
    template_name = 'component_messages.html'


class ComponentFormInputView(TemplateView):
    template_name = 'component_form_input.html'

class ComponentFormValidationView(TemplateView):
    template_name = 'component_form_validation.html'

class ComponentFormLayoutView(TemplateView):
    template_name = 'component_form_layout.html'

class ComponentHeaderView(TemplateView):
    template_name = 'component_header.html'

class ComponentButtonView(TemplateView):
    template_name = 'component_button.html'

class ComponentTableView(TemplateView):
    template_name = 'component_table.html'

class ComponentLabelView(TemplateView):
    template_name = 'component_label.html'

class ComponentPanelView(TemplateView):
    template_name = 'component_panel.html'


class ComponentBreadcrumbView(TemplateView):
    template_name = 'component_breadcrumb.html'



