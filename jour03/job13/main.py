from os.path import exists
import matplotlib.pyplot as plt
import numpy as np

filename = 'data.txt'
lowercase = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
    'e': 0,
    'f': 0,
    'g': 0,
    'h': 0,
    'i': 0,
    'j': 0,
    'k': 0,
    'l': 0,
    'm': 0,
    'n': 0,
    'o': 0,
    'p': 0,
    'q': 0,
    'r': 0,
    's': 0,
    't': 0,
    'u': 0,
    'v': 0,
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0
}
uppercase = {
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0,
    'E': 0,
    'F': 0,
    'G': 0,
    'H': 0,
    'I': 0,
    'J': 0,
    'K': 0,
    'L': 0,
    'M': 0,
    'N': 0,
    'O': 0,
    'P': 0,
    'Q': 0,
    'R': 0,
    'S': 0,
    'T': 0,
    'U': 0,
    'V': 0,
    'W': 0,
    'X': 0,
    'Y': 0,
    'Z': 0,
}

letters = []

if exists(filename):
    file = open(filename)
    text = file.read()
    file.close()

    words = text.split()
    for word in words:
        for i in lowercase:
            if word[0] == lowercase[i]:
                letters[lowercase[i]] += 1

        for i in uppercase:
            if word[0] == uppercase[i]:
                letters[uppercase[i]] += 1

    print(letters)

    # compte it de lower + it de up = letter
    for i in range(25):
        letters.append(lowercase[i] + uppercase[i])

    print(letters)

else:
    print("File does not exist.")

fig, ax = plt.subplots()

count = list(letters.keys())
letter = list(letters.values())

plt.bar(range(len(letters)), letter, tick_label=count)
plt.grid()
plt.show()
