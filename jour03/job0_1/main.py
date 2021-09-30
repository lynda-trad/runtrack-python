from os.path import exists
if not exists("output.txt"):
    file = open("output.txt", "x")
    file.write(input("Entrez une chaine de caractères "))
    test = file.read()
    print(test)
    file.close()
else:
    print("File already exists.")
    