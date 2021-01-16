'''Dice roller and random item finder'''

import json
import random

json_file_name = "TestMagicItems.json"

#Pull data from file
def get_data(file_name):
    #Open json file
    with open(file_name) as data_dict:
        #Return json obj as a dict
        return json.load(data_dict)

#Roll how_manyDkind of dice
def roll_dice(how_many, kind):
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

#Choose a random entry from a dict
def random_entry(data_dict):
    #Key list
    key_list = []
    #Get a list of keys
    for key in data_dict:
        key_list.append(key)
    
    #Roll random number
    index = random.randint(0,len(data_dict) - 1)

    #Use index and key list to locate key and value in the dict
    return (str(key_list[index]) + ": " + str(data_dict[key_list[index]]))


def main():
    print ("Hello World!")

    print ("Random Item from the test file: ", random_entry(get_data(json_file_name)))
    print ("Data in file: ", get_data(json_file_name))
    print ("Dice roller: ", roll_dice(3,12))

#This little chunk of code allows this python program to be either used directly or imported into another program
if __name__ == "__main__":
    main()    