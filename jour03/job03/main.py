from os.path import exists
import re

number = int(input("Entrez le taille de mots que vous recherchez\n"))
count = 0
filename = 'data.txt'

if exists(filename):
    file = open(filename)
    text = file.read()
    file.close()
    words = text.split()
    for word in words:
        if len(word) == number:
            count += 1
    print(count)
else:
    print("File does not exist.")