import numpy as np

n = int(input("Entrez un nombre pour la taille : n x n\n"))
plateau = np.tile('O', (n, n))
print(plateau, "\n")
ini = 0


def game(n, init):
    pions = n

    if init == 0:
        x = 0
        y = 0
        plateau[x][y] = 'X'
        init = 1

    if n % 2 == 0 and n > 3:
        print(plateau, "\n")
        while y != n and pions != 0:
            if x + 2 <= n and y + 1 <= n:
                plateau[x + 2][y + 1] = 'X'
                x += 1
                y += 1
            elif x + 2 > n >= y + 1:
                y += 1
                x = 0
            else:
                return True
        return True
    else:
        print("Impossible de placer les dames sur un plateau", n, "x", n)
        return False


print("Placement des pieces possible : ", game(n, ini))
print(plateau)
