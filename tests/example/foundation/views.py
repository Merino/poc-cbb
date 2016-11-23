from panels.layouts import Breadcrumb, Button
from panels.views import TemplateAdminView

from .utils import FONT_AWESOME_ICON_LIST

class FoundationIndex(TemplateAdminView):
    """
    """
    template_name = 'foundation_index.html'


class FoundationColors(TemplateAdminView):
    """
    """
    page_header_title = 'Color'
    page_header_navigation = [
        Breadcrumb(title='Dashboard',  href='/'),
        Breadcrumb(title='Foundation', href='/foundation/'),
    ]

    template_name = 'foundation_colors.html'


class FoundationGrid(TemplateAdminView):
    """
    """
    page_header_title = 'Grid'
    page_header_navigation = [
        Breadcrumb(title='Dashboard',  href='/'),
        Breadcrumb(title='Foundation', href='/foundation/'),
    ]

    template_name = 'foundation_grid.html'


class FoundationIcons(TemplateAdminView):
    """
    """
    page_header_title = 'Icons'
    page_header_navigation = [
        Breadcrumb(title='Dashboard',  href='/'),
        Breadcrumb(title='Foundation', href='/foundation/'),
    ]

    template_name = 'foundation_icons.html'

    def icon_list(self):
        return FONT_AWESOME_ICON_LIST

    def get_context_data(self, **kwargs):
        kwargs = super(FoundationIcons, self).get_context_data(**kwargs)
        kwargs.update({
            'icon_list': self.icon_list()
        })

        return kwargs


class FoundationLayout(TemplateAdminView):
    """
    """
    page_header_title = 'Layout'
    page_header_navigation = [
        Breadcrumb(title='Dashboard',  href='/'),
        Breadcrumb(title='Foundation', href='/foundation/'),
    ]

    template_name = 'foundation_layout.html'


class FoundationLoading(TemplateAdminView):
    """
    """
    page_header_title = 'Loading'
    page_header_navigation = [
        Breadcrumb(title='Dashboard',  href='/'),
        Breadcrumb(title='Foundation', href='/foundation/'),
    ]

    template_name = 'foundation_loading.html'


class FoundationMotions(TemplateAdminView):
    """
    """
    page_header_title = 'Motions'
    page_header_navigation = [
        Breadcrumb(title='Dashboard',  href='/'),
        Breadcrumb(title='Foundation', href='/foundation/'),
    ]
    template_name = 'foundation_motions.html'


class FoundationMessaging(TemplateAdminView):
    """
    """
    page_header_title = 'Messaging'
    page_header_navigation = [
        Breadcrumb(title='Dashboard',  href='/'),
        Breadcrumb(title='Foundation', href='/foundation/'),
    ]
    template_name = 'foundation_messaging.html'


class FoundationTypography(TemplateAdminView):
    """
    """
    page_header_title = 'Typography'
    page_header_navigation = [
        Breadcrumb(title='Dashboard',  href='/'),
        Breadcrumb(title='Foundation', href='/foundation/'),
    ]
    template_name = 'foundation_typography.html'


class FoundationNavigation(TemplateAdminView):
    """
    """
    page_header_title = 'Navigation'
    page_header_navigation = [
        Breadcrumb(title='Dashboard',  href='/'),
        Breadcrumb(title='Foundation', href='/foundation/'),
    ]
    template_name = 'foundation_navigation.html'


class FoundationVoiceAndTone(TemplateAdminView):
    """
    """
    page_header_title = 'Voice & Tone'
    page_header_navigation = [
        Breadcrumb(title='Dashboard',  href='/'),
        Breadcrumb(title='Foundation', href='/foundation/'),
    ]
    template_name =  'foundation_voice_and_tone.html'