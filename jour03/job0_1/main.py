from os.path import exists
if not exists("output.txt"):
    file = open("output.txt", "a+")
    file.write(input("Entrez une chaine de caractères "))
    file.close()

else:
    print("File already exists.")

file = open("output.txt")
print(file.read())
