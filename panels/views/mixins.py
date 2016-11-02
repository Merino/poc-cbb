from django.contrib.auth.mixins import LoginRequiredMixin


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