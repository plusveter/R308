from part_a import *

class Bibliotheque:
    # Ressemble à une base de donnée

    def __init__(self):
        self.livres = {}
        self.utilisateurs = {}

    def ajouter_livre(self, livre): # enregistre le livre dans la class
        self.livres[livre.titre] = livre

    def ajouter_utilisateur(self, utilisateur): # enregistre l'utilisateur dans la classe
        self.utilisateurs[utilisateur.nom] = utilisateur

    def emprunter(self, nom, titre):
        if nom not in self.utilisateurs:
            print("Utilisateur inconnu") ; return False

        if titre not in self.livres:
            print("Livre inconnu") ; return False

        utilisateur = self.utilisateurs[nom]
        livre = self.livres[titre]

        if utilisateur.emprunter_livre(livre):
            print("Livre emprunté avec succès") ; return True

        print("Livre déjà emprunté")
        return False

    def rendre(self, nom, titre):
        if nom not in self.utilisateurs:
            print("Utilisateur inconnu") ; return False

        if titre not in self.livres:
            print("Livre inconnu"); return False

        utilisateur = self.utilisateurs[nom]
        livre = self.livres[titre]

        if utilisateur.rendre_livre(livre):
            print("Livre rendu avec succès"); return True

        print("Impossible de rendre ce livre"); return False

    def afficher_livres(self):
        for livre in self.livres.values(): # Check si il y a des livre disponible of emprunté
            if livre.disponible:
                print(livre.titre, "- Disponible")
            else:
                print(livre.titre, "- Emprunté par", livre.emprunteur)


if __name__ == "__main__":
    biblio = Bibliotheque() # Création de la lib bibliothèque

    livre1 = Livre("1984", "Orwell", 1949)
    livre2 = Livre("Le Petit Prince", "Saint-Exupéry", 1943)

    ana = Utilisateur("Ana")
    leo = Utilisateur("Léo")

    biblio.ajouter_livre(livre1)
    biblio.ajouter_livre(livre2)

    biblio.ajouter_utilisateur(ana)
    biblio.ajouter_utilisateur(leo)

    biblio.emprunter("Ana", "1984")
    biblio.emprunter("Léo", "1984")

    biblio.afficher_livres()
    biblio.rendre("Ana", "1984")
    biblio.emprunter("Léo", "1984")
    biblio.emprunter("Ana", "Harry Potter")
