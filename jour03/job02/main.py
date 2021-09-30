from os.path import exists
import re

filename = "data.txt"

if exists(filename):
    file = open(filename)
    text = file.read()
    count = text.split()
    for word in count:
        if word == ''
    print(len(count))
    file.close()
else:
    print("File does not exist.")