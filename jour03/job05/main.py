from os.path import exists
import matplotlib.pyplot as plt
import numpy as np

filename = 'data.txt'
lowercase = [  # lowercase
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z'
]
uppercase = [
    # uppercase
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M',
    'N',
    'O',
    'P',
    'Q',
    'R',
    'S',
    'T',
    'U',
    'V',
    'W',
    'X',
    'Y',
    'Z'
]

letters = {}

if exists(filename):
    file = open(filename)
    text = file.read()
    file.close()

    for i in range(25):
        count = text.count(lowercase[i]) + text.count(uppercase[i])
        letters[lowercase[i]] = count

    print(letters)
else:
    print("File does not exist.")

fig, ax = plt.subplots()

count = list(letters.keys())
letter = list(letters.values())

plt.bar(range(len(letters)), letter, tick_label=count)
plt.grid()
plt.show()
