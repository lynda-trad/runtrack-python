# List generator

# Print a list
def printList(mylist):
    listing = ""
    for index in range(len(mylist)):
        listing = listing + str(mylist[index]) + " "
    print(listing)


# Check if list needs sorting
def checkList(mylist):
    for it in range(0, len(mylist)):
        if mylist[it] > mylist[it + 1]:
            return False
        elif it == len(mylist) - 1:
            if mylist[it] < mylist[it + 1]:
                return True
            else:
                return False


# Sorting
def sorting(mylist):
    sorted = False
    while not sorted:
        for it in range(0, len(mylist) - 1):
            if mylist[it] > mylist[it + 1]:
                print(mylist[it], " at index ", it, " and ", mylist[it + 1], " at index ", it + 1)

                temp = mylist[it]
                mylist[it] = mylist[it + 1]
                mylist[it + 1] = temp
                printList(mylist)
        sorted = checkList(mylist)
        print(sorted)
    return mylist


# Test
length = 5
mylist = list()
while length != 0:
    print(length, " number(s) left.\n")
    mylist.append(int(input("Please enter a number.")))
    length -= 1

printList(mylist)

sorting(mylist)

printList(mylist)
