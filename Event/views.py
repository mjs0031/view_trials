""" Python Package Support """
import random

""" Django Package Support """
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import detail, list, TemplateView
from django.core.exceptions import PermissionDenied

""" Internal Package Support """
from Event.models import Event

""" Allow templates to request current URL """
from django.shortcuts import render_to_response
from django.template import RequestContext

"""
 Event/views.py

 Author:      Matthew J Swann
 Version:     1.0
 Last Update: 2014-06-06
 Update By:   Matthew J Swann

"""

def index(request):
    events_all = Event.objects.all()
    dict = {
            'events_all' : events_all,
            }
    return render_to_response('all_events.html', dict)


def event_home(request):
    return render_to_response('ajax_event_home.html')


def event_search(request, search_string):
    found   = True 
    results = Event.objects.filter(company_tag=search_string)
    
    if not results:
        results = Event.objects.all()
        found   = False
    
    return render_to_response('ajax_event_render.html', {
                                'results' : results,
                                'found'   : found,
                                })

#
# TemplateView Logic Trial
#
class hello_world(TemplateView):
    template_name = 'hello.html'
    

class fifty_fifty_failure(TemplateView):
    template_name = 'failure.html'
    
    def dispatch(self, request, *args, **kwargs):
        if random.choice([True, False]):
            raise PermissionDenied
        return super(fifty_fifty_failure, self). dispatch(request, *args, **kwargs)


#
# Mixin Trial
#
class fifty_fifty_failure_mixin(object):
    def dispatch(self, request, *args, **kwargs):
        if random.choice([True, False]):
            raise PermissionDenied
        return super(fifty_fifty_failure_mixin, self). dispatch(request, *args, **kwargs)


class fifty_fifty_failure_two(fifty_fifty_failure_mixin, TemplateView):
    template_name = 'failure.html'
    

#
# DetailView Trial
#
class event_detail_view(detail.DetailView):
    template_name = 'event_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(event_detail_view, self).get_context_data(**kwargs)
        context['event'] = Event.objects.get(pk=self.kwargs.get('event.id', None))
        return context
    
