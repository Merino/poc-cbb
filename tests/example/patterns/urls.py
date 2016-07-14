from django.conf.urls import url

from .views import PatternLayoutBlank, PatternLayoutList, PatternLayoutRecord, PatternLayoutFocus, PatternDataTable, PatternLogin, PatternPageHeader

urlpatterns = [
    url(r'^layout-blank/', PatternLayoutBlank.as_view()),
    url(r'^layout-list/', PatternLayoutList.as_view()),
    url(r'^layout-record/', PatternLayoutRecord.as_view()),
    url(r'^layout-focus/', PatternLayoutFocus.as_view()),

    url(r'^datatable/', PatternDataTable.as_view()),
    url(r'^login/', PatternLogin.as_view()),
    url(r'^pageheader/', PatternPageHeader.as_view()),
]

