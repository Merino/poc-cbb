from django.views.generic.base import TemplateView

from .mixins import AdminRequiredMixin


class TemplateAdminView(AdminRequiredMixin, TemplateView):
    """
    """
    pass