# Check if list needs sorting
def checkList(mylist):
    for it in range(len(mylist)-1):
        if mylist[it] > mylist[it + 1]:
            return False
    return True


# Sorting
def sorting(mylist):
    sorted = False
    while not sorted:
        for it in range(len(mylist) - 1):
            if mylist[it] > mylist[it + 1]:
                temp = mylist[it]
                mylist[it] = mylist[it + 1]
                mylist[it + 1] = temp
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

print("List before sorting : ", mylist)

sorting(mylist)

print("List after sorting: ", mylist)