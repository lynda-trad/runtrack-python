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
        for it in range(len(self.oeuvre)):
            self.oeuvre[it].printL()

    def ecrireUnLivre(self, titre):
        new = Livre(titre, self)
        self.oeuvre.append(new)


class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

    def printL(self):
        print("~", self.titre, "par", self.auteur.prenom, self.auteur.nom)


# Test class Auteur
A1 = Auteur("Jeff", "Vandermeer")
A1.sepresenter()
A1.listerOeuvre()
print("\n")

#Apres ajout des livres
A1.ecrireUnLivre("Annihilation")
A1.listerOeuvre()