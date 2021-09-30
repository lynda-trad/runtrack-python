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

print("Avant la mise en pourcentage: \n", length)

# Percentage
total = sum(length.values())

print(total)

for le in length:
    length[le] = float(length[le]) / total * 100

print("Apres la mise en pourcentage: \n", length)

fig, ax = plt.subplots()

count = list(length.keys())
longueur = list(length.values())

plt.bar(length.keys(), longueur, tick_label=count)
plt.grid()
plt.show()