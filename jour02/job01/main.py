class Person:

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
        print(self.prenom, " ", self.nom)


# Test du constructeur
P1 = Person("Louis", "Armstrong")
P1.sepresenter()

# Test des get et set
print("Prenom : ", P1.getPrenom())
print("Nom : ", P1.getNom())

P1.setPrenom("Jeff")
P1.setNom("Vandermeer")
P1.sepresenter()