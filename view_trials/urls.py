from django.conf.urls import patterns, include, url

from Event.views import (hello_world, fifty_fifty_failure, fifty_fifty_failure_two,
                         event_detail_view)

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'view_trials.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello_world.as_view(), name='hello_world'),
    url(r'^failure/$', fifty_fifty_failure.as_view(), name='fifty_fifty_failure'),
    url(r'^failure_two/$', fifty_fifty_failure_two.as_view(), name='fifty_fifty_failure_two'),
    
    # Event related
    url(r'^index/$', 'Event.views.index', name='index'),
    url(r'^event/search/$', 'Event.views.event_home', name='event_home'),
    url(r'^event/search/([\w-]+)/$', 'Event.views.event_search', name='event_search'),
    url(r'^event/(?P<event_id>\d+)/$', event_detail_view.as_view()),
)
