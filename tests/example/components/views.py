from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView

from panels.layouts import Breadcrumb
from panels.views import TemplateAdminView


class ComponentIndexView(TemplateAdminView):
    page_header_title = 'Components'
    page_header_navigation = [
        Breadcrumb(title='Dashboard',  href='/'),
    ]

    template_name = 'component_index.html'


class ComponentNotificationView(TemplateAdminView):
    page_header_title = 'Notification'
    page_header_navigation = [
        Breadcrumb(title='Dashboard',  href='/'),
        Breadcrumb(title='Components', href='/components/'),
    ]

    template_name = 'component_notification.html'


class ComponentFormInputView(TemplateAdminView):
    template_name = 'component_form_input.html'


class ComponentFormValidationView(TemplateAdminView):
    template_name = 'component_form_validation.html'


class ComponentFormLayoutView(TemplateAdminView):
    template_name = 'component_form_layout.html'


class ComponentHeaderView(TemplateAdminView):
    template_name = 'component_header.html'


class ComponentButtonView(TemplateAdminView):
    template_name = 'component_button.html'


class ComponentTableView(TemplateAdminView):
    page_header_title = 'Table'
    page_header_navigation = [
        Breadcrumb(title='Dashboard',  href='/'),
        Breadcrumb(title='Components', href='/components/'),
    ]

    template_name = 'component_table.html'


class ComponentLabelView(TemplateAdminView):
    template_name = 'component_label.html'


class ComponentPanelView(TemplateAdminView):
    template_name = 'component_panel.html'


class ComponentBreadcrumbView(TemplateAdminView):
    template_name = 'component_breadcrumb.html'



