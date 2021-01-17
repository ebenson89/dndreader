'''Dice roller and random item finder'''

import json
import random
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic

qtCreatorFile = "mainwindow.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
json_file_path = "datafiles\TestMagicItems.json" #Test File

class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.roll_dice_button.clicked.connect(self.roll_dice)
        self.random_item_button.clicked.connect(self.random_entry)

    #Pull data from file
    def get_data(self, file_name):
        #Open json file
        with open(file_name) as data_dict:
            #Return json obj as a dict
            return json.load(data_dict)

    #Roll how_manyDkind of dice
    def roll_dice(self):
        #User Input
        how_many = int(self.how_many_box.text())
        kind = int(self.kind_box.text())
        #Total variables
        total = 0
        output_str = str(how_many) + "d" + str(kind) + ": "
        
        #Roll the choosen dice how_many times
        for x in range (1, how_many + 1):
            #Pick a random number
            number = random.randint(1,kind)
            #Add number to the total
            total += number
            #Add the number to the output string
            output_str = output_str + (str(number))
            #Add addition symbols between the numbers in the string
            if 0 < x < how_many:
                output_str = output_str + (" + ")

        #Add on the total to the output string
        output_str = output_str + (" = ") + str(total)
        #Print out string
        self.results_output.setText(output_str)

    #Choose a random item from the file
    def random_entry(self):
        #Grab the data from the choosen file
        data_dict = self.get_data(json_file_path)
        #Randomly choose a key
        key = random.choice(list(data_dict.keys()))
        #Print out key and value in a string
        self.random_item_output.setText(key + ": " + data_dict[key])

#def main():
    #print ("Hello World!")

    #print ("Random Item from the test file: ", random_entry(get_data(json_file_name)))
    #print ("Data in file: ", get_data(json_file_name))
    #print ("Dice roller: ", roll_dice(3,12))

#This little chunk of code allows this python program to be either used directly or imported into another program
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())