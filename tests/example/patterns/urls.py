from django.conf.urls import url

from .views import PatternDashboard, PatternDataTable, PatternLogin, PatternPageHeader

urlpatterns = [
    url(r'^dashboard/', PatternDashboard.as_view()),
    url(r'^datatable/', PatternDataTable.as_view()),
    url(r'^login/', PatternLogin.as_view()),
    url(r'^pageheader/', PatternPageHeader.as_view()),
]