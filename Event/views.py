""" Python Package Support """
# Not Applicable

""" Django Package Support """
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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

