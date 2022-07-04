# Works!
# And it includes a dictionary
from tkinter import Tk, simpledialog, messagebox

def lees_uit_bestand():
    with open('hoofdstad_data.txt') as bestand:
        for lijn in bestand:
            lijn = lijn.rstrip('\n')
            land, stad = lijn.split('/')
            de_wereld[land] = stad
            
def schrijf_naar_bestand(naam_land, naam_stad):
    with open('hoofdstad_data.txt', 'a') as bestand:
        bestand.write('\n' + naam_land + '/' + naam_stad)
        
print('Vraag het de expert - Hoofdsteden van de wereld')
root = Tk()
root.withdraw()
de_wereld = {}

lees_uit_bestand()

while True:
    vraag_land = simpledialog.askstring('Land', 'Typ de naam van een land:')
    
    if vraag_land in de_wereld:
        resultaat = de_wereld[vraag_land]
        messagebox.showinfo('Antwoord', 'De hoofdstad van '+ vraag_land + ' is '+ resultaat + '!')
    else:
        nieuwe_stad = simpledialog.askstring('Vertel het me', 'Ik weet het niet! '+ 'Wat is de hoofdstad van '+ vraag_land + '?')
        de_wereld[vraag_land] = nieuwe_stad
        schrijf_naar_bestand(vraag_land, nieuwe_stad)
        
root.mainloop()