from __future__ import print_function
from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
import random 

SCOPES = 'https://www.googleapis.com/auth/calendar.addons.execute'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
GCAL = discovery.build('calendar', 'v3', http=creds.authorize(Http()))

"""----------------------------------------------------------- List of emails ----------------------------------------- """

list_email = [] 




temp_email = list_email 

if len(list_email) % 2 == 0:
   n = len(list_email)/2
else:
   n = (len(list_email) - 1)/2  



i = 0
while i < n: 
        
    x = random.choice(temp_email)
    temp_email.remove(x) 
    y = random.choice(temp_email)
    temp_email.remove(y)  
    GMT_OFF = '-07:00'      # PDT/MST/GMT-7
    


    EVENT = {
        'summary': 'Social - WFH Small Talk',
        'Description': 'A Creative Platform Technology (CPT) experiment to foster social communication by arbitarily connecting 2 people in the Ignite hub',
        'start':  {'dateTime': '2020-04-07T15:00:00%s' % GMT_OFF},
        'end':    {'dateTime': '2020-04-07T15:10:00%s' % GMT_OFF},
        'attendees': [
            {'email': x},
            {'email': y},
        ],
        'hangoutLink': 'meet.google.com/wsv-amin-ozh', 
        'guestsCanModify': True,  
        'conferenceData': {
            'createRequest': {'requestId': "7qxalsvy0e"}
        }
    }
    e = GCAL.events().insert(calendarId='Ignitesf.calendar@gmail.com',
        sendNotifications=True, body=EVENT, conferenceDataVersion = 1 ).execute()

    print('''*** %r event added:
       Start: %s
       End:   %s''' % (e['summary'].encode('utf-8'),
           e['start']['dateTime'], e['end']['dateTime']))
    i = i+1
    print(x,y,i,n)

