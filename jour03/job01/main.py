from os.path import exists

if exists("output.txt"):
    file = open("output.txt")
    print(file.read())
    file.close()
else:
    print("File does not exist.")

