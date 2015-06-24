from django.conf.urls import include, url

from .views import GridTemplateView, BlocksTemplateView, IconTemplateView, TypoTemplateView, FormTemplateView, DashboardView

urlpatterns = [
    url(r'^/grid/', GridTemplateView.as_view()),
    url(r'^/blocks/', BlocksTemplateView.as_view()),
    url(r'^/typography/', TypoTemplateView.as_view()),
    url(r'^/icons/', IconTemplateView.as_view()),
    url(r'^/forms/', FormTemplateView.as_view()),
    url(r'/', DashboardView.as_view()),
]