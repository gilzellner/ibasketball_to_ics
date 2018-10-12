import xlrd
from ics import Calendar, Event
from datetime import datetime, timedelta
import dateutil

workbook = xlrd.open_workbook('/home/gilzellner/Downloads/exported_data_2018-10-12_12-53.xls')
sheet = workbook.sheet_by_index(0)
schedule = []
for rx in range(sheet.nrows):
    if 'number' in str(sheet.row(rx)[0]):
        game = {}
        # game['row'] = rx
        # game['raw'] = sheet.row(rx)
        # game['index'] = str(sheet.row(rx)[0]).replace('text:', '')
        game['date'] = str(sheet.row(rx)[2]).replace('text:', '').replace('u', '').replace('\'', '')
        game['time'] = str(sheet.row(rx)[3]).replace('text:', '').replace('u', '').replace('\'', '')
        game['home'] = str(sheet.row(rx)[4]).replace('text:', '').encode('utf-8')
        game['away'] = str(sheet.row(rx)[5]).replace('text:', '').encode('utf-8')
        game['location'] = str(sheet.row(rx)[6]).replace('text:', '').encode('utf-8')
        schedule.append(game)

for game in schedule:
    game['start'] = datetime.strptime(game['date'] + ' ' + game['time'], '%d-%m-%Y %H:%M:%S')\
        .replace(tzinfo=dateutil.tz.tzoffset('IST', 3*60*60))
    # print(game['start'])
    game['end'] = game['start'] + timedelta(hours=2)
    # print(game['end'])

c = Calendar()
for game in schedule:
    e = Event()
    e.name = game['away'] + ' at ' + game['home']
    e.begin = game['start']
    e.end = game['end']
    e.location = game['location']
    c.events.add(e)
# [<Event 'My cool event' begin:2014-01-01 00:00:00 end:2014-01-01 00:00:01>]
with open('my.ics', 'w') as my_file:
    my_file.writelines(c)

with open('my.ics', 'r') as my_file:
    print my_file.read()
