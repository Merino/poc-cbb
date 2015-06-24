from django.conf.urls import patterns, include, url

from example.layout.views import DashboardView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'example.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^layout', include('example.layout.urls')),
    url(r'^pages',  include('example.pages.urls')),

    url(r'^views', include('example.views.urls')),
    url(r'', DashboardView.as_view())
)
