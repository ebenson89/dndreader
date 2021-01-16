'''The GUI class aka bluprint'''

import tkinter as tk
import random

class GUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.widgets()

    #Make all of the things on the GUI
    def widgets(self):
        
        #Entry for the number of dice rolled
        self.number_of_dice = tk.Entry()
        self.number_of_dice.pack(side = "left")

        #Lable between the two entry boxes
        self.d = tk.Label(self)
        self.d["text"] = "d"
        self.d.pack(side = "left")

        #Entry for the kind of dice rolled
        self.kind_of_dice = tk.Entry()
        self.kind_of_dice.pack(side = "left")

        #Roll the Dice button
        self.roll = tk.Button(self)
        self.roll["text"] = "Roll the Dice!"
        #Where the button is located on the GUI
        self.roll.pack(side = "bottom")

    #Roll how_many D kind of dice
    def roll_dice(self, how_many, kind):
        total = 0
        output_str = str(how_many) + "d" + str(kind) + ": "
        
        #Roll the choosen dice how_many times
        for x in range (1, how_many + 1):
            number = random.randint(1,kind)
            total += number
            output_str = output_str + (str(number))
            if 0 < x < how_many:
                output_str = output_str + (" + ")

        output_str = output_str + (" = ") + str(total)

        return (output_str)

        

#Still don't know what this does
root = tk.Tk()
#Object constructer
gui = GUI(master=root)
#Launches GUI
gui.mainloop()