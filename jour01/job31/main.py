# Print list
def printList(mylist):
    listing = ""
    for index in range(len(mylist)):
        listing = listing + str(mylist[index]) + " "
    print(listing)


# Rounding
def rounding(note):
    temp = note
    strikes = 3
    while strikes != 0:
        if note % 5 == 0:
            return note
        else:
            note += 1
        strikes -= 1

    if note % 5 == 0:
        return note
    else:
        return temp


def failedOrNot(notes):
    for it in range(len(notes)):
        if notes[it] > 40:
            if notes[it] % 5 != 0:
                notes[it] = rounding(notes[it])
    return notes


# Test
notes = list()
notes = [40, 23, 57, 92, 100, 46]
print("Original List : ")
printList(notes)

notes = failedOrNot(notes)

print("New list after rounding : ")
printList(notes)
