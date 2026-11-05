
class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = True
        self.emprunteur = None

    def afficher(self): # Affichage des information que le livre poosède
        print(self.titre, "-", self.auteur, "-", self.annee)
        print("Disponible :", self.disponible)

    def emprunter(self, nom): # fonction d'emprunt
        
        if self.disponible: # si il est disponible, prendre le nom du client + changer la variable disponible
            self.disponible = False 
            self.emprunteur = nom
            return True 
        return False

    def rendre(self):
        if not self.disponible: # si il n'est pas disponible, effacer le nom du client + changer la variable disponible
            self.disponible = True
            self.emprunteur = None
            return True
        return False



class Utilisateur:
    def __init__(self, nom):
        self.nom = nom
        self.emprunts = []

    def emprunter_livre(self, livre):
        if livre.emprunter(self.nom): # fait la demande + vérifie si c'est possible d'emprunter un livre
            self.emprunts.append(livre) # ajoute la class livre dans la liste
            return True
        return False

    def rendre_livre(self, livre):
        if livre in self.emprunts: # vérifie si le livre est dans sa list
            if livre.rendre():
                self.emprunts.remove(livre) # retire la classe livre dans la liste
                return True
        return False

    def afficher_emprunts(self): 
        print("Emprunts de", self.nom)
        for livre in self.emprunts:
            print("-", livre.titre)


if __name__ == "__main__": # lance le test seulement si le fichier est lancé principalement & non par d'autre fichier py

    livre1 = Livre("1984", "Orwell", 1949)

    ana = Utilisateur("Ana")
    leo = Utilisateur("Léo")

    print(ana.emprunter_livre(livre1))
    print(leo.emprunter_livre(livre1))

    ana.afficher_emprunts()

    print(ana.rendre_livre(livre1))
    print(leo.emprunter_livre(livre1))
