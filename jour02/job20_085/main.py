# Dimensions ixj

# Player Yellow J
# Player Rouge  R

class Board:
    def __init__(self, i, j):
        self.grille = [['O' for i in range(i)] for j in range(j)]
        self.i = i
        self.j = j

    def play(self, column, color):
        print("")

    def print(self):
        for row in self.grille:
            for elem in row:
                print(elem, end=' ')
            print()


# Generation et affichage
game = Board(5, 5)
game.print()
