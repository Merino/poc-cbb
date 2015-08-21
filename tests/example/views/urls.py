from django.conf.urls import include, url

from .views import ListDataView

urlpatterns = [
#    url(r'^/form/single/', SingleFormView.as_view()),
#    url(r'^/inline/single/', SingleInlineView.as_view()),

    url(r'^/list/', ListDataView.as_view()),
]