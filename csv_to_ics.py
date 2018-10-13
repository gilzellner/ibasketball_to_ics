import csv
import tempfile, os
from datetime import datetime, timedelta
import dateutil
from icalendar import Calendar, Event

schedule = []
with open('schedule.csv', 'rb') as csvfile:
    schedule_file_reader = csv.reader(csvfile, delimiter=',')
    for row in schedule_file_reader:
        try:
            int(row[0])
        except:
            continue
        if row[0] is not '':
            game = {}
            game['date'] = row[2]
            game['time'] = row[3]
            game['home'] = row[4]
            game['away'] = row[5]
            game['location'] = row[6]
            game['start'] = datetime.strptime(game['date'] + ' ' + game['time'], '%d-%m-%Y %H:%M:%S') \
                .replace(tzinfo=dateutil.tz.tzoffset('XXX', 3*60*60))
            game['end'] = game['start'] + timedelta(hours=2)
            schedule.append(game)
            print game

c = Calendar()

for game in schedule:
    e = Event()
    e.add('dtstart', game['start'])
    e.add('dtend', game['end'])
    e.add('summary', game['away'] + ' vs ' + game['home'])
    e.add('location', game['location'])
    c.add_component(e)#

directory = tempfile.mkdtemp()
f = open(os.path.join(directory, '/Users/gilzellner/dev/ibasketball_to_ics/calendar.ics'), 'wb')
f.write(c.to_ical())
f.close()
