from django.views.generic.base import TemplateView

from .mixins import AdminRequiredMixin, PageHeaderMixin


class TemplateAdminView(AdminRequiredMixin, PageHeaderMixin, TemplateView):
    """
    """

    def get_context_data(self, **kwargs):
        kwargs = super(TemplateAdminView, self).get_context_data(**kwargs)
        kwargs.update({
            'header': self.get_page_header(**kwargs)
        })
        return kwargs