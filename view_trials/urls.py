from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'view_trials.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', 'Event.views.index', name='index'),
    url(r'^event/search/$', 'Event.views.event_home', name='event_home'),
    url(r'^event/search/([\w-]+)/$', 'Event.views.event_search', name='event_search'),
)
