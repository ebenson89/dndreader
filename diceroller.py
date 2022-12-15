'''Dice roller and random item finder'''

import json
import random
import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *  #Ignore wildcare error no impact on functionality
from PyQt5.QtGui import QIntValidator

start_folder = "datafiles\\"
json_file_path = ""
qtCreatorFile = "mainwindow.ui" # GUI Design file
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.how_many_box.setValidator(QIntValidator(0, 100, self))
        self.kind_box.setValidator(QIntValidator(0, 100, self))
        self.files_in_data_folder()
        self.roll_dice_button.clicked.connect(self.roll_dice)
        self.random_item_button.clicked.connect(self.random_entry)
        self.files_list_output.clicked.connect(self.choose_file)

    def choose_file(self, qmodelindex):
        """Choose a file from the data folder"""
        global json_file_path
        item = self.files_list_output.currentItem()
        json_file_path = start_folder + item.text()
    
    def get_data(self, file_name):
        """Pull data from file"""
        # Open json file
        with open(file_name) as data_dict:
            # Return json obj as a dict
            return json.load(data_dict)

    def roll_dice(self):
        """Roll how_many d kind of dice"""
        # User Input
        how_many = self.how_many_box.text()
        kind = self.kind_box.text()

        # Check if user input present
        if how_many == "" or kind == "":
            self.results_output.setText("Please Enter dice")
        else:
            # Total variables
            total = 0
            output_str = how_many + "d" + kind + ": "
            
            # Roll the choosen dice how_many times
            for x in range (1, int(how_many) + 1):
                # Pick a random number
                number = random.randint(1, int(kind))
                # Add number to the total
                total += number
                # Add the number to the output string
                output_str = output_str + (str(number))
                # Add addition symbols between the numbers in the string
                if 0 < x < int(how_many):
                    output_str = output_str + (" + ")

            # Add on the total to the output string
            output_str = output_str + (" = ") + str(total)
            # Print out string
            self.results_output.setText(output_str)

    def random_entry(self):
        """Choose a random item from the file"""
        # Check if user has selected a file
        if json_file_path == "":
            self.random_item_output.setText("Please choose a file.")
        else:
            # Grab the data from the choosen file
            data_dict = self.get_data(json_file_path)
            # Randomly choose a key
            key = random.choice(list(data_dict.keys()))
            # Print out key and value in a string
            self.random_item_output.setText(key + ": " + data_dict[key])

    def files_in_data_folder(self):
        """Choose a file in the database"""
        for _ , _ ,file_names in os.walk("datafiles"):
            if file_names[0][-5:] == ".json":
                self.files_list_output.insertItems(0, file_names)

#This little chunk of code allows this python program to be either used directly or imported into another program
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())