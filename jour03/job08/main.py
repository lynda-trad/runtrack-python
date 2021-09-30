from os.path import exists
import matplotlib.pyplot as plt
import numpy as np

filename = 'data.txt'
length = {}

if exists(filename):
    file = open(filename)
    text = file.read()
    file.close()
    words = text.split()
    for word in words:
        if len(word) not in length:
            length[len(word)] = 1
        else:
            length[len(word)] += 1

else:
    print("File does not exist.")

print(length)

fig, ax = plt.subplots()

count = list(length.keys())
longueur = list(length.values())

plt.bar(range(len(length)), longueur, tick_label=count)
plt.grid()
plt.show()

