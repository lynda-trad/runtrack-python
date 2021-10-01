def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


number = int((input("Entrez un nombre")))
print("Son factoriel est ", factorial(number))
