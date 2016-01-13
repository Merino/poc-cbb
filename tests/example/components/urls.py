from django.conf.urls import url

from .views import ComponentBreadcrumb, ComponentButtonGroupView, ComponentButtonView

urlpatterns = [
    url(r'^breadcrumb/', ComponentBreadcrumb.as_view()),
    url(r'^buttons/', ComponentButtonView.as_view()),
    url(r'^buttonsgroup/', ComponentButtonGroupView.as_view()),
]