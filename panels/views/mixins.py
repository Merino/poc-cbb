from django.contrib.auth.mixins import LoginRequiredMixin

from ..layouts import Header

class AdminRequiredMixin(LoginRequiredMixin):
    """
    """

    def dispatch(self, request, *args, **kwargs):
        """
        Returns True if the given HttpRequest has permission to view
        the admin page
        """
        if request.user.is_active and request.user.is_staff:
            return super(AdminRequiredMixin, self).dispatch(request, *args, **kwargs)
        else:
            return self.handle_no_permission()


class PageHeaderMixin(object):
    """
    """
    page_header_title = ''
    page_header_actions = []
    page_header_navigation = []

    def get_page_header_navigation(self, **kwargs):
        """
            [
                Breadcrumb(link='/', title='Dashboard'),
                Breadcrumb(link='/app/', title='Application'),
                Breadcrumb(link='/app/model/', title='Model'),
            ]
        """
        return self.page_header_navigation

    def get_page_header_title(self, **kwargs):
        """
        """
        return self.page_header_title

    def get_page_header_actions(self, **kwargs):
        """
        """
        return self.page_header_actions

    def get_page_header(self, **kwargs):
        """
        """
        header = Header()
        header.title = self.get_page_header_title(**kwargs)
        header.navigation = self.get_page_header_navigation(**kwargs)
        header.actions = self.get_page_header_actions(**kwargs)

        return header