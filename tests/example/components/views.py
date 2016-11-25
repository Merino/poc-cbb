from vesper.layouts import Breadcrumb
from vesper.views import TemplateAdminView


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


class ComponentFormElementsView(TemplateAdminView):
    page_header_title = 'Form Elements'
    page_header_navigation = [
        Breadcrumb(title='Dashboard',  href='/'),
        Breadcrumb(title='Components', href='/components/'),
    ]
    template_name = 'component_form_elements.html'


class ComponentFormValidationView(TemplateAdminView):
    page_header_title = 'Form Validation'
    page_header_navigation = [
        Breadcrumb(title='Dashboard',  href='/'),
        Breadcrumb(title='Components', href='/components/'),
    ]
    template_name = 'component_form_validation.html'


class ComponentFormLayoutView(TemplateAdminView):
    page_header_title = 'Form Layout'
    page_header_navigation = [
        Breadcrumb(title='Dashboard',  href='/'),
        Breadcrumb(title='Components', href='/components/'),
    ]

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


class ComponentCardsView(TemplateAdminView):
    page_header_title = 'Cards'
    page_header_navigation = [
        Breadcrumb(title='Dashboard',  href='/'),
        Breadcrumb(title='Components', href='/components/'),
    ]

    template_name = 'component_cards.html'


class ComponentBreadcrumbView(TemplateAdminView):
    template_name = 'component_breadcrumb.html'



