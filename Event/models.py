""" Python Package Support """
from datetime import date, datetime, time
from pytz import timezone

""" Django Package Support """
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.timezone import utc
from localflavor.us import models as us_models

""" Internal Package Support """
# Not aplicable

"""
 
 Event/models.py

 Author:      Matthew J Swann
 Version:     1.0
 Last Update: 2014-06-06
 Update By:   Matthew J Swann 

"""

#TABLE: Event
class Event(models.Model):
    """
    EVENT CLASS - abstraction for a unique spatial-temporal occurrence that
    necessitates the services of one or more interpreters
    """
    #Keyed fields
    company_tag          = models.CharField(max_length=16, verbose_name = 'Creator\'s Company Tag')
    creator_tag          = models.CharField(max_length=16, verbose_name = 'Creator\'s Tag')
    languages            = models.CharField(max_length=64, blank=True, verbose_name = 'Languages')
    #Natural fields
    title                = models.CharField(max_length=128, blank=True, verbose_name = 'Title')
    date_created         = models.DateTimeField(default=datetime.now().replace(tzinfo=utc), verbose_name = 'Date Created')
    date_time_start      = models.DateTimeField(null=True, verbose_name = 'Date and Time Start')
    date_time_end        = models.DateTimeField(null=True, verbose_name = 'Date and Time End')
    timezone             = models.CharField(max_length=64, default='America/Chicago')
    date                 = models.DateField(verbose_name = 'Date')
    sessionStart         = models.TimeField(verbose_name = 'Session Start')
    sessionEnd           = models.TimeField(verbose_name = 'Session End')
    addressLineOne       = models.CharField(max_length=128, verbose_name = 'Address Line 1')
    addressLineTwo       = models.CharField(max_length=128, verbose_name = 'Address Line 2', blank=True)
    addressLineThree     = models.CharField(max_length=128, verbose_name = 'Address Line 3', blank=True)
    city                 = models.CharField(max_length=32, verbose_name = 'City')
    state                = us_models.USStateField(verbose_name = 'State')
    zipCode              = models.CharField(max_length=10, verbose_name = 'Zip Code',
                            validators=[RegexValidator(r'^\d{5}(-\d{4})?$')])
    
    class Meta:
        verbose_name        = "Event"
        verbose_name_plural = "Events"
        
        
    def save(self, *args, **kwargs):
        """
        Save override. Been in place a while. Normalizes date field
        """    
        self.sessionStart = _clean_time(self.sessionStart)
        self.sessionEnd   = _clean_time(self.sessionEnd)
        self.date         = _clean_date(self.date)
        
        # temporary solution to duplicative date fields until they can be paired off
                
        self.date_time_start = datetime(self.date.year, 
                                        self.date.month,
                                        self.date.day,
                                        self.sessionStart.hour,
                                        self.sessionStart.minute,
                                        self.sessionEnd.second)
        
        self.date_time_end   = datetime(self.date.year, 
                                        self.date.month,
                                        self.date.day,
                                        self.sessionEnd.hour,
                                        self.sessionEnd.minute,
                                        self.sessionEnd.second)
                                        
        zone = timezone(self.timezone)
            
        self.date_time_end   = zone.localize(self.date_time_end)
        self.date_time_start = zone.localize(self.date_time_start)
            
        self.date_time_end   = pack_time_utc(self.date_time_end)
        self.date_time_start = pack_time_utc(self.date_time_start)

        super(Event, self).save(*args, **kwargs)
        
        
"""
 {
  BLOCK: Support
 }
"""

def _clean_date(the_date):
    """
    Changes a string representation of a date object into an actual date object.
    
    @param the_date : String representation of a date, or simply a date object.
    
    @return { date } : Date object, possibly from a string representation
    """
    if isinstance(the_date, str):
        try:
            array = the_date.split('-')

            the_date = date(int(array[0]), int(array[1]), int(array[2]))

        except:
            raise ValidationError('_clean_date() improper date construction')

    elif not ( isinstance(the_date, date) or the_date == None ):
        raise ValidationError('_clean_date() requires date or string representation of date')

    return the_date


def _clean_datetime(the_datetime):
    """
    Changes a string representation of a datetime object into an actual datetime object.
    
    @param the_datetime : String representation of datetime, or simply a datetime object.
    
    @return { datetime } : Datetime object, possibly from a string representation
    """
    if isinstance(the_datetime, str):
        try:
            the_array = the_datetime.split(' ')

            the_date = the_array[0].split('-') 
            the_time = the_array[1].split(':')
            
            the_datetime = datetime( int(the_date[0]), int(the_date[1]), int(the_date[2]),
                                 int(the_time[0]), int(the_time[1]), int(the_time[2]) )

        except:
            raise ValidationError('_clean_datetime() improper datetime construction')

    elif not ( isinstance(the_datetime, datetime) or the_datetime == None ):
        raise ValidationError('_clean_datetime() requires datetime or string representation of date')

    return the_datetime


def _clean_time(the_time):
    """
    Changes a string representation of a time object into an actual time object.
    
    @param the_time : String representation of time, or simply a time object.
    
    @return { time } : Time object, possibly from a string representation
    """
    if isinstance(the_time, str):
        try:
            array = the_time.split(':')

            the_time = time(int(array[0]), int(array[1]), int(array[2]))

        except:
            raise ValidationError('_clean_time() improper time construction')

    elif not ( isinstance(the_time, time) or the_time == None ):
        raise ValidationError('_clean_time() requires time or string representation of time')
    
    return the_time


def pack_time_utc(date_time_object):
    """
    Converts the current datetime object to UTC time and stamps the timezone
    information accordingly.
    
    @param date_time_object : Unvalidated datetime object
    
    @return { datetime } : Returns the manufactured datetime object 
    """
    if not isinstance(date_time_object, datetime):
        raise TypeError('pack_time() requires a datetime object first')
    
    utc_zone = timezone('UTC')
    
    normal = date_time_object.astimezone(utc_zone)
    
    return normal
