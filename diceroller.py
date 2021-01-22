'''Dice roller and random item finder'''

import json
import random
import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *

start_folder = "datafiles\\"
json_file_path = ""
qtCreatorFile = "mainwindow.ui" # GUI Design file
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.files_in_data_folder()
        self.roll_dice_button.clicked.connect(self.roll_dice)
        self.random_item_button.clicked.connect(self.random_entry)
        self.files_list_output.clicked.connect(self.choose_file)

    #Choose a file from the data folder
    def choose_file(self, qmodelindex):
        global json_file_path
        item = self.files_list_output.currentItem()
        json_file_path = start_folder + item.text()
        print (json_file_path)
    
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

        #Check if user has selected a file
        if json_file_path == "":
            self.random_item_output.setText("Please choose a file.")
        else:
            #Grab the data from the choosen file
            data_dict = self.get_data(json_file_path)
            #Randomly choose a key
            key = random.choice(list(data_dict.keys()))
            #Print out key and value in a string
            self.random_item_output.setText(key + ": " + data_dict[key])

    #Choose a file in the database
    def files_in_data_folder(self):

        for _ , _ ,file_names in os.walk("datafiles"):
            if file_names[0][-5:] == ".json":
                self.files_list_output.insertItems(0, file_names)


#This little chunk of code allows this python program to be either used directly or imported into another program
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())