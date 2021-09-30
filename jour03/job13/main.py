from os.path import exists
import matplotlib.pyplot as plt
import numpy as np

filename = 'data.txt'
alphabet = {
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
}
letters = {}

if exists(filename):
    file = open(filename)
    text = file.read()
    file.close()
    text.lower()

    words = text.split()
    for word in words:
        for al in alphabet:
            if word[0] == al:
                if al in letters:
                    letters[al] += 1
                else:
                    letters[al] = 1

else:
    print("File does not exist.")

#Percentage
print("Avant la mise en pourcentage: \n", letters)

total = sum(letters.values())

print(total)

for le in letters:
    letters[le] = float(letters[le]) / total * 100

print("Apres la mise en pourcentage: \n", letters)

# Hist creation
fig, ax = plt.subplots()

count = list(letters.keys())
letter = list(letters.values())

plt.bar(letters.keys(), letter, tick_label=count)
plt.grid()
plt.show()
