def power(x, n):
    if n == 1:
        return x
    else:
        return x * power(x, n - 1)


number = int(input("Entrez un nombre"))
puissance = int(input("Entrez la puissance que vous souhaitez"))
print("La puissance de number est", power(number, puissance))
