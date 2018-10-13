So the ibasketball.co.il lets you export schedules, but they are not easy to use.
they export excel files, which nobody uses today anyway and manually entering on your phone sucks.
this script take a CSV converted file and converts it to an ICS file you can import on your iphone or android or calendar.

usage:

export the schedule you want, you should get an excel file.
convert it to csv using something like gnumeric (cli)

pip install icalendar csv
python csv_to_ics.py -i /home/gil/schedule.csv -o  /home/gil/schedule.ics
