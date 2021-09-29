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
        print(self.prenom, self.nom)


class Auteur(Personne):
    def __init__(self, prenom, nom, oeuvre):
        super().__init__(prenom, nom)
        self.oeuvre = oeuvre

    # Liste les oeuvres
    def listerOeuvre(self):
        print(self.oeuvre)

    def ecrireUnLivre(self, titre, auteur):
        new = Livre.__init__(titre, auteur)
        self.oeuvre.append(new)


class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

    def print(self):
        print(self.titre, "par ", self.auteur.sepresenter())


# Test class Auteur
A1 = Auteur("Jeff", "Vandermeer", {"Annihilation", "Autorité"})
A1.sepresenter()
A1.listerOeuvre()

# Test class Livre
A1.ecrireUnLivre("Acceptation", A1)

A1.listerOeuvre()

