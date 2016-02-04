from django.conf.urls import url

from .views import PatternDataTable, PatternLogin, PatternPageHeader

urlpatterns = [
    url(r'^datatable/', PatternDataTable.as_view()),
    url(r'^login/', PatternLogin.as_view()),
    url(r'^pageheader/', PatternPageHeader.as_view()),
]