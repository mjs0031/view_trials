""" Python Package Support """
# Not Applicable

""" Django Package Support """
# Not Applicable

""" Internal Package Support """
from Event.models import Event

"""

 Event/event_import.py
 
 Author      : Matthew J Swann
 Version     : 1.0
 Last Update : 2014-06-05
 Update By   : Matthew J Swann
 
 """
 
class EventImport(object): 
    
    def __init__(self, scriptName=None):
       
             
        # 1
        Event.objects.create(
            company_tag    = 'B-1',
            date           = '2019-01-02',
            sessionStart   = '5:00:00',
            sessionEnd     = '8:00:00',
            addressLineOne = '345 W. Magnolia Ave',
            addressLineTwo = 'Room 3139A',
            city           = 'Auburn',
            state          = 'AL',
            zipCode        = '36832',
            creator_tag    = 'P-4'   
                )
        
        # 2
        Event.objects.create(
            company_tag    = 'B-2',
            date           = '2019-06-07',
            sessionStart   = '6:15:00',
            sessionEnd     = '17:30:00',
            addressLineOne = '345 W. Magnolia Ave',
            addressLineTwo = 'Room 3139A',
            city           = 'Auburn',
            state          = 'AL',
            zipCode        = '36832',
            creator_tag    = 'N-2'   
                )
        
        # 3
        Event.objects.create(
            company_tag    = 'B-3',
            date           = '2019-06-09',
            sessionStart   = '00:00:00',
            sessionEnd     = '18:00:15',
            addressLineOne = '345 W. Magnolia Ave',
            addressLineTwo = 'Room 3139A',
            city           = 'Auburn',
            state          = 'AL',
            zipCode        = '36832',
            creator_tag    = 'N-1'   
                )

        #------------------------------------------
        #
        # ASSIGNMENT AND INVOICE DATA TEST DATA
        #
        #------------------------------------------
                
        # 4
        Event.objects.create(
            company_tag    = 'B-5',
            date           = '2018-02-28',
            sessionStart   = '12:00:00',
            sessionEnd     = '14:00:00',
            addressLineOne = '345 W. Magnolia Ave',
            addressLineTwo = 'Room 3139A',
            city           = 'Auburn',
            state          = 'AL',
            zipCode        = '36832',
            creator_tag    = 'N-2'   
                )
        
        # 5
        Event.objects.create(
            company_tag    = 'B-5',
            date           = '2018-03-28',
            sessionStart   = '13:00:00',
            sessionEnd     = '13:45:00',
            addressLineOne = '345 W. Magnolia Ave',
            addressLineTwo = 'Room 3139A',
            city           = 'Auburn',
            state          = 'AL',
            zipCode        = '36832',
            creator_tag    = 'N-2'   
                )
        
        # 6
        Event.objects.create(
            company_tag    = 'B-5',
            date           = '2018-02-27',
            sessionStart   = '13:00:00',
            sessionEnd     = '17:00:00',
            addressLineOne = '345 W. Magnolia Ave',
            addressLineTwo = 'Room 3139A',
            city           = 'Auburn',
            state          = 'AL',
            zipCode        = '36832',
            creator_tag    = 'N-2'   
                )

        # 7
        Event.objects.create(
            company_tag    = 'B-5',
            date = '2018-02-14',
            sessionStart = '10:00:00',
            sessionEnd   = '10:15:00',
            addressLineOne = '345 W. Magnolia Ave',
            addressLineTwo = 'Room 3139A',
            city = 'Aubrun',
            state ='AL',
            zipCode = '36832',
            creator_tag    = 'N-2'   
                )
        # 8
        Event.objects.create(
            company_tag    = 'B-5',
            date = '2018-02-13',
            sessionStart = '15:00:00',
            sessionEnd   = '17:00:00',
            addressLineOne = '345 W. Magnolia Ave',
            addressLineTwo = 'Room 3139A',
            city = 'Aubrun',
            state ='AL',
            zipCode = '36832',
            creator_tag    = 'N-2'   
                )
        # 9
        Event.objects.create(
            company_tag    = 'B-5',
            date = '2018-02-13',
            sessionStart = '12:00:00',
            sessionEnd   = '12:10:00',
            addressLineOne = '345 W. Magnolia Ave',
            addressLineTwo = 'Room 3139A',
            city = 'Aubrun',
            state ='AL',
            zipCode = '36832',
            creator_tag    = 'N-2'   
                )
        
        #------------------------------------------
        #
        # SCHEDULE/HISTORY/PERSONNEL DATA TEST DATA
        #
        #------------------------------------------
        
        # 10
        Event.objects.create(
            company_tag    = 'B-10',
            date           = '2015-12-31',
            sessionStart   = '12:00:00',
            sessionEnd     = '12:10:00',
            addressLineOne = '4 Yawkey Way',
            addressLineTwo = 'Home Team Dugout',
            city           = 'Boston',
            state          = 'MA',
            zipCode        = '02215',
            creator_tag    = 'N-1'   
                )

        
        # 11
        Event.objects.create(
            company_tag    = 'B-11',
            date           = '2015-12-31',
            sessionStart   = '12:00:00',
            sessionEnd     = '12:10:00',
            addressLineOne = '4 Yawkey Way',
            addressLineTwo = 'Home Team Dugout',
            city           = 'Boston',
            state          = 'MA',
            zipCode        = '02215',
            creator_tag    = 'N-1'   
                )
        
        
        # 12
        Event.objects.create(
            company_tag    = 'B-12',
            date           = '2015-12-31',
            sessionStart   = '12:00:00',
            sessionEnd     = '12:10:00',
            addressLineOne = '4 Yawkey Way',
            addressLineTwo = 'Home Team Dugout',
            city           = 'Boston',
            state          = 'MA',
            zipCode        = '02215',
            creator_tag    = 'N-1'   
                )

        
        # 13
        Event.objects.create(
            company_tag    = 'B-13',
            date           = '2015-12-31',
            sessionStart   = '12:00:00',
            sessionEnd     = '12:10:00',
            addressLineOne = '4 Yawkey Way',
            addressLineTwo = 'Home Team Dugout',
            city           = 'Boston',
            state          = 'MA',
            zipCode        = '02215',
            creator_tag    = 'N-1'   
                )

        
        # 14
        Event.objects.create(
            company_tag    = 'B-14',
            date           = '2015-12-31',
            sessionStart   = '12:00:00',
            sessionEnd     = '12:10:00',
            addressLineOne = '4 Yawkey Way',
            addressLineTwo = 'Home Team Dugout',
            city           = 'Boston',
            state          = 'MA',
            zipCode        = '02215',
            creator_tag    = 'N-1'   
                )

        
        # 15
        Event.objects.create(
            company_tag    = 'B-10',
            date           = '2015-12-31',
            sessionStart   = '12:00:00',
            sessionEnd     = '12:10:00',
            addressLineOne = '4 Yawkey Way',
            addressLineTwo = 'Home Team Dugout',
            city           = 'Boston',
            state          = 'MA',
            zipCode        = '02215',
            creator_tag    = 'N-1'   
                )

        
        # 16
        Event.objects.create(
            company_tag    = 'B-11',
            date           = '2015-12-31',
            sessionStart   = '12:00:00',
            sessionEnd     = '12:10:00',
            addressLineOne = '4 Yawkey Way',
            addressLineTwo = 'Home Team Dugout',
            city           = 'Boston',
            state          = 'MA',
            zipCode        = '02215',
            creator_tag    = 'N-1'   
                )

        
        # 17
        Event.objects.create(
            company_tag    = 'B-12',
            date           = '2015-12-31',
            sessionStart   = '12:00:00',
            sessionEnd     = '12:10:00',
            addressLineOne = '4 Yawkey Way',
            addressLineTwo = 'Home Team Dugout',
            city           = 'Boston',
            state          = 'MA',
            zipCode        = '02215',
            creator_tag    = 'N-1'   
                )

        
        # 18
        Event.objects.create(
            company_tag    = 'B-13',
            date           = '2015-12-31',
            sessionStart   = '12:00:00',
            sessionEnd     = '12:10:00',
            addressLineOne = '4 Yawkey Way',
            addressLineTwo = 'Home Team Dugout',
            city           = 'Boston',
            state          = 'MA',
            zipCode        = '02215',
            creator_tag    = 'N-1'   
                )

        
        # 19
        Event.objects.create(
            company_tag    = 'B-14',
            date           = '2015-12-31',
            sessionStart   = '12:00:00',
            sessionEnd     = '12:10:00',
            addressLineOne = '4 Yawkey Way',
            addressLineTwo = 'Home Team Dugout',
            city           = 'Boston',
            state          = 'MA',
            zipCode        = '02215',
            creator_tag    = 'N-1'   
                )


        
        