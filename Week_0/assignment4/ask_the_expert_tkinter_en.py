# Works!
# And it includes a dictionary
from tkinter import Tk, simpledialog, messagebox

def read_from_file():
    with open('data_capital_city.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            country, city = line.split('/')
            the_world[country] = city
            
def write_to_file(name_country, name_city):
    with open('data_capital_city.txt', 'a') as file:
        file.write('\n' + name_country + '/' + name_city)
        
print('Ask the expert - Capital Cities of the World')
root = Tk()
root.withdraw()
the_world = {}

read_from_file()

while True:
    ask_country = simpledialog.askstring('country', 'Type the name of a country:')
    
    if ask_country in the_world:
        result = the_world[ask_country]
        messagebox.showinfo('Answer', 'The capital city of '+ ask_country + ' is '+ result + '!')
    else:
        new_city = simpledialog.askstring('Tell me', 'I do not know! '+ 'What is the capital city of '+ ask_country + '?')
        the_world[ask_country] = new_city
        write_to_file(ask_country, new_city)
        
root.mainloop()