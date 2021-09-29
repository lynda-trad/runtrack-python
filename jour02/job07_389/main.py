class Personne:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom

    def getPrenom(self):
        return self.prenom

    def getNom(self):
        return self.nom

    def setPrenom(self, prenom):
        self.prenom = prenom

    def setNom(self, nom):
        self.nom = nom

    def sepresenter(self):
        print("Auteur : ", self.prenom, self.nom)


class Auteur(Personne):
    def __init__(self, prenom, nom):
        super().__init__(prenom, nom)
        self.oeuvre = []

    # Liste les oeuvres
    def listerOeuvre(self):
        print("Oeuvres de l'auteur : ")
        for livre in self.oeuvre:
            livre.printL()

    def ecrireUnLivre(self, titre):
        new = Livre(titre, self)
        self.oeuvre.append(new)


class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

    def printL(self):
        print("~", self.titre, "par", self.auteur.prenom, self.auteur.nom)


class Client(Personne):
    def __init__(self, prenom, nom):
        super().__init__(prenom, nom)
        self.collection = {}

    # affiche livres du client
    def inventaire(self):
        print("Le client", self.prenom, self.nom, "a dans sa collection", self.collection)

    def ajoutLivre(self, nom):
        if nom in self.collection:
            self.collection[nom] += 1
        else:
            self.collection[nom] = 1


class Bibliotheque:
    def __init__(self, nom, collection):  # collection = { titre : quantité int }
        self.nom = nom
        self.collection = collection

    def acheterLivre(self, auteur, nom, quantite):
        if nom in auteur.oeuvre:
            if nom in self.collection:
                self.collection[nom] += quantite
            else:
                self.collection[nom] = quantite

    def inventaire(self):
        print("La bibliotheque répertorie les livres :", self.collection)

    def louer(self, client, nom):
        # Look for the book
        if nom in self.collection:
            if self.collection[nom] != 0:
                self.collection[nom] -= 1
                client.ajoutLivre(nom)
            else:
                print("Sorry we do not have any", nom, "books left")
        else:
            print("We do not have", nom, "in our library !")

    def rendreLivres(self, client):
        for livre in client.collection:
            if livre.titre in self.collection:
                self.collection[livre.titre] += 1
            else:
                self.collection[livre.titre] = 1


# Creation d'un auteur
A1 = Auteur("Jeff", "Vandermeer")
A1.sepresenter()
# Ajout des livres a l'oeuvre de l'auteur
A1.ecrireUnLivre("Annihilation")
A1.ecrireUnLivre("Autorité")
A1.ecrireUnLivre("Acceptation")
A1.listerOeuvre()

if "Acceptation" in A1.oeuvre:
    print("Acceptation est bien une oeuvre de ", A1.nom, "\n")

# Creation de bibliotheque
collection = {
    "Annihilation": 2,
    "Autorité": 4,
}
bibliotheque = Bibliotheque("Joliette", collection)
bibliotheque.inventaire()

# Ajout du livre a la bibliotheque
bibliotheque.acheterLivre(A1, "Acceptation", 3)
print("Ajout du livre Acceptation en 3 exemplaires à la bibliothèque")
bibliotheque.inventaire()

# Creation de client
C1 = Client("Gilles", "Valentine")
C1.ajoutLivre("Lord of the Rings")
C1.inventaire()
