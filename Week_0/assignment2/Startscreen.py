# Works
from tkinter import *
import tkinter as tk

# root window
root = tk.Tk()
#root.geometry('250x600')
root.geometry('250x250')

root.resizable(False,False)
root.title('Tkinter Demo')

# Text
text = Text(root, height=1)
text.insert(END, 'What has to be assembled? ')
text.pack()

# Canvas widget
c = Canvas(root, width=250, height=160, bd=3, bg = 'white', confine = True, cursor  = 'dot', highlightcolor='blue', relief='raised')
circle = c.create_oval(4, 6, 75, 75, outline = 'blue', fill='blue')
circle = c.create_oval(79, 6, 154, 75, outline = 'yellow', fill='yellow')
circle = c.create_oval(158, 6, 233, 75, outline = 'red', fill='red')

vierkant = c.create_rectangle(4, 80 , 75, 151, outline='red', fill='red')
vierkant = c.create_rectangle(79, 80 , 154, 151, outline='blue', fill='blue')
vierkant = c.create_rectangle(158, 80 , 233, 151, outline='yellow', fill='yellow')

c.pack()

# exit button
exit_button = tk.Button( root, text='Exit', command = lambda: root.quit()) 
exit_button.pack( ipadx = 5, ipady = 5, expand = True) # Pack is one alternative, grid another

root.mainloop()
        