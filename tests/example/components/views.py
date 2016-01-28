from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView


class ComponentIndexView(TemplateView):
    template_name = 'component_index.html'


class ComponentMessagesView(TemplateView):
    template_name = 'component_messages.html'

class ComponentFormView(TemplateView):
    template_name = 'component_form.html'

class ComponentFormButton(TemplateView):
    template_name = 'component_button.html'
