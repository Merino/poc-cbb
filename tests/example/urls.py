from django.conf.urls import patterns, include, url

from example.foundation.views import FoundationIndex

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'example.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^layout', include('example.layout.urls')),
    #url(r'^pages',  include('example.pages.urls')),

    url(r'^foundation/', include('example.foundation.urls')),
    url(r'^components/', include('example.components.urls')),
    url(r'^patterns/', include('example.patterns.urls')),
    #url(r'^views', include('example.views.urls')),
    url(r'^$', FoundationIndex.as_view()),

    url(r'^views/', admin.site.urls),
    url(r'^nested_admin/', include('nested_admin.urls')),
)
