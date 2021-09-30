from os.path import exists
import re

filename = "data.txt"
count = 0
special = ['.', ',', ';', '!', '\'', '\n', '?', '<', '>', '-', '_', '\\', '\"', ')', '(', 'é', '~', '`', '{', '}', '&', '=', '+', '%', '$', '£', '¨', '*', '²', ' ', '|', '#', '°', 'µ', '@']

if exists(filename):
    file = open(filename)
    text = file.read()
    words = text.split()
    for word in words:
        if word not in special: # caracteres speciaux
            count += 1

    print(count)
    file.close()
else:
    print("File does not exist.")