# Works
from tkinter import Tk, Canvas
from datetime import date, datetime

def ontvang_gebeurtenissen():
    lijst_gebeurtenissen = []
    with open('gebeurtenissen.txt') as bestand:
        for lijn in bestand:
            lijn = lijn.rstrip('\n')
            huidige_gebeurtenis = lijn.split(',')
            gebeurtenis_datum = datetime.strptime(huidige_gebeurtenis[1], '%d/%m/%y').date()
            huidige_gebeurtenis[1] = gebeurtenis_datum
            lijst_gebeurtenissen.append(huidige_gebeurtenis)
    return lijst_gebeurtenissen

def dagen_tussen_datums(datum1, datum2):
    tijd_tussen = str(datum1 - datum2)
    aantal_dagen = tijd_tussen.split(' ')
    return aantal_dagen[0]

root = Tk()
c = Canvas(root, width = 800, height = 800, bg='black')
c.pack()
c.create_text(100, 50, anchor = 'w', fill = 'orange', font = 'Arial 20 bold underline', text = 'My countdowncalendar')

gebeurtenissen = ontvang_gebeurtenissen()
vandaag = date.today()

verticale_ruimte = 100
for gebeurtenis in gebeurtenissen:
    gebeurtenis_naam = gebeurtenis[0]
    dagen_tot = dagen_tussen_datums(gebeurtenis[1], vandaag)
    weergave = 'Het is %s dagen tot %s' % (dagen_tot, gebeurtenis_naam)
    c.create_text(100, verticale_ruimte, anchor = 'w', fill = 'lightblue', font = 'Arial 20 bold underline', text = weergave)
    verticale_ruimte = verticale_ruimte + 30
    
root.mainloop()