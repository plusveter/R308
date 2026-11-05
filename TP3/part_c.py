# Import de la librairy
import csv 
from part_b import *

class BibliothequeCSV(Bibliotheque):

    def sauvegarder(self):
        # Ouvre le fichier (Il créer un nouveau si il n'existe pas grace à "+")
        with open("livres.csv", "w+", newline="", encoding="utf-8") as fichier:
            # Définit la première ligne (aka le titre)
            writer = csv.DictWriter(fichier, fieldnames=["titre", "auteur", "annee", "disponible", "emprunteur"]) 

            
            writer.writeheader()
            for livre in self.livres.values():
                writer.writerow({
                    "titre": livre.titre,
                    "auteur": livre.auteur,
                    "annee": livre.annee,
                    "disponible": livre.disponible,
                    "emprunteur": livre.emprunteur or ""
                })

        print("Bibliothèque sauvegardée")

    def charger(self):
        try:
            # Essay de lire le fichier, en cas d'erreur le programme peut continué de fonctionné
            with open("livres.csv", "r", encoding="utf-8", newline="") as fichier:
                reader = csv.DictReader(fichier)
                for ligne in reader: # Récupère les donnée sur les livres
                    livre = Livre( ligne["titre"], ligne["auteur"], int(ligne["annee"]) )
                    self.ajouter_livre(livre)
                    if ligne["disponible"] == "False":
                        nom = ligne["emprunteur"]
                        if nom:
                            if nom not in self.utilisateurs: self.ajouter_utilisateur(Utilisateur(nom))
                            self.utilisateurs[nom].emprunter_livre(livre)

            print("Bibliothèque chargée")

        except FileNotFoundError:
            print("Aucune sauvegarde trouvée")


if __name__ == "__main__":

    # Utilisé la classe enfant
    biblio = BibliothequeCSV()

    # Méthods héritées de Bibliotheque
    biblio.ajouter_livre(Livre("1984", "Orwell", 1949))
    biblio.ajouter_utilisateur(Utilisateur("Ana"))
    biblio.emprunter("Ana", "1984")

    # Nouvel méthode de BibliothequeCSV
    biblio.sauvegarder()

    # Test le chargement
    biblio2 = BibliothequeCSV()
    biblio2.charger()

    biblio2.afficher_livres()
    biblio2.rendre("Ana", "1984")
