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
        print("Auteur : ", self.prenom, self.nom, "\n")


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

    def estDansLoeuvre(self, nom):
        for livre in self.oeuvre:
            if livre.getTitre() == nom:
                return True
        return False


class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

    def getTitre(self):
        return self.titre

    def printL(self):
        print("~", self.titre, "par", self.auteur.prenom, self.auteur.nom)


class Client(Personne):
    def __init__(self, prenom, nom):
        super().__init__(prenom, nom)
        self.collection = {}

    # affiche livres du client
    def inventaire(self):
        print("Le client", self.prenom, self.nom, "a dans sa collection", self.collection, "\n")

    def ajoutLivre(self, livre):
        if livre in self.collection:
            self.collection[livre] += 1
        else:
            self.collection[livre] = 1


class Bibliotheque:
    def __init__(self, nom, collection):  # collection = { titre : quantité int }
        self.nom = nom
        self.collection = collection

    def acheterLivre(self, auteur, nom, quantite):
        if auteur.estDansLoeuvre(nom):
            for livre in self.collection:
                if livre.getTitre == nom:
                    self.collection[nom] += quantite
                #else:
                    # on cree le livre
                    #self.collection[nom] = quantite
        else:
            print("Cet auteur n'a pas ecrit ce livre.")

    def inventaire(self):
        print("La bibliotheque répertorie :")
        for livre in self.collection:
            print("-", self.collection[livre], "exemplaires de :")
            livre.printL()

        print("\n")


    def louer(self, client, nom):
        # Look for the book
        for livre in self.collection:
            if livre.getTitre() == nom:
                if self.collection[livre] != 0:
                    self.collection[livre] -= 1
                    client.ajoutLivre(nom)

    def rendreLivres(self, client):
        for livre in client.collection:
            if livre.titre in self.collection:
                self.collection[livre.titre] += 1
            else:
                self.collection[livre.titre] = 1


# Creation d'un auteur
print("---Creation d'un auteur---")
A1 = Auteur("Jeff", "Vandermeer")
A1.sepresenter()
# Ajout des livres a l'oeuvre de l'auteur
A1.ecrireUnLivre("Annihilation")
A1.ecrireUnLivre("Autorité")
A1.ecrireUnLivre("Acceptation")

# Creation de bibliotheque
print("---Creation d'une bibliotheque---")
collection = {
    A1.oeuvre[0]: 2,    #Annihilation
    A1.oeuvre[1]: 4,    #Autorité
}
bibliotheque = Bibliotheque("Joliette", collection)
bibliotheque.inventaire()

# Creation de client
print("---Creation d'un client---")
C1 = Client("Gilles", "Valentine")
C1.ajoutLivre("Lord of the Rings")
C1.inventaire()


# Test louer
print("---Le client loue Annihilation---")
bibliotheque.louer(C1, "Annihilation")
C1.inventaire()
print("---La bibliotheque est mise à jour---")
bibliotheque.inventaire()

# Ajout d'un livre a la bibliotheque
print("---Ajout du livre Acceptation en 3 exemplaires à la bibliothèque---\n")
bibliotheque.acheterLivre(A1, "Acceptation", 3)
bibliotheque.inventaire()

