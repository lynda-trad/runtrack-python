class Board:
    def __init__(self, i, j):
        self.grille = [['O' for h in range(i)] for w in range(j)]
        self.height = i
        self.width = j

    def play(self, color, column):
        if color == "Rouge":
            c = 'R'
            print("You played R")
        elif color == "Jaune":
            c = 'J'
            print("You played J")
        elif column > self.width:
            return print("Please enter a valid column")
        else:
            return print("Please enter a valid color")

        # Drop the coin
        height = self.height - 1
        column -= 1
        while height != 0:
            print("dans le while")
            if self.grille[height][column] == '0':
                print(" Height : ", height, "Column: ", column, "\n")
                self.grille[height][column] == c
                height = 0
            height -= 1

    def print(self):
        for row in self.grille:
            for elem in row:
                print(elem, end=' ')
            print()

    def verification(self):
        for row in self.grille:
            break
            # verif ligne

            # verif colonne

            # verif diagonale gauche


# Generation et affichage
game = Board(5, 5)
game.print()
winner = False

while not winner:
    color = input("Qui joue ? Jaune ou Rouge ?")
    column = int(input("Veuillez entrer la colonne."))
    game.play(color, column)
    game.print()