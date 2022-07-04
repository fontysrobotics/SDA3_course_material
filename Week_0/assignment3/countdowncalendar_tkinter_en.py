# Works
from tkinter import Tk, Canvas
from datetime import date, datetime

def recieve_events():
    list_events = []
    with open('events.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            current_event = line.split(',')
            event_date = datetime.strptime(current_event[1], '%d/%m/%y').date()
            current_event[1] = event_date
            list_events.append(current_event)
    return list_events

def days_between_dates(datum1, datum2):
    time_between = str(datum1 - datum2)
    number_of_days = time_between.split(' ')
    return number_of_days[0]

root = Tk()
c = Canvas(root, width = 800, height = 800, bg='black')
c.pack()
c.create_text(100, 50, anchor = 'w', fill = 'orange', font = 'Arial 20 bold underline', text = 'My countdowncalendar')

events = recieve_events()
today = date.today()

vertical_space = 100
for gebeurtenis in events:
    event_name = gebeurtenis[0]
    days_until = days_between_dates(gebeurtenis[1], today)
    weergave = 'It is %s days up until %s' % (days_until, event_name)
    c.create_text(100, vertical_space, anchor = 'w', fill = 'lightblue', font = 'Arial 20 bold underline', text = weergave)
    vertical_space = vertical_space + 30
    
root.mainloop()