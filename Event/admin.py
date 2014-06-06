""" Python Package Imports """
# Not Applicable

""" Django Package Support """
from django.contrib import admin

"""        Internal Package Support          """
""" -- IMPORTED AT APPROPRIATE SUBSECTION -- """


""" 

 event/admin.py
 
 Author:      Matthew J Swann
 Version:     1.0
 Last Update: 2014-06-05
 Update by:   Matthew J Swann

  
 """


class EventAdmin(admin.ModelAdmin):
    list_display  = ('id', 'date', 'company_tag', 'city','state')
    list_filter   = ('state',)
    search_fields = ['date', 'company_tag', 'state', 'creator_tag', 'date_created']
    ordering      = ['date', 'city', 'state']
    fieldsets     = (               
        ( 'Advanced options', {
            'classes': ('wide', 'extrapretty'),
            'fields' : ('date_created', 'creator_tag', 'company_tag', 'date', 'date_time_start', 
                        'date_time_end', 
                        'title', 
                        'sessionStart', 'sessionEnd', 'addressLineOne', 'addressLineTwo', 'city', 
                        'state', 'zipCode')
                 }),)   
    
from Event.models import (
                    Event
                        )
admin.site.register(Event, EventAdmin)
