from django.conf.urls import url

from .views import PatternDataTable, PatternLogin, PatternPageHeader, PatternLayoutContentOnly, PatternLayoutContentSidebar

urlpatterns = [
    url(r'^layout-contentonly/', PatternLayoutContentOnly.as_view()),
    url(r'^layout-content-sidebar/', PatternLayoutContentSidebar.as_view()),
    url(r'^datatable/', PatternDataTable.as_view()),
    url(r'^login/', PatternLogin.as_view()),
    url(r'^pageheader/', PatternPageHeader.as_view()),
]

