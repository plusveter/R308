class Personne:
    def __init__(self, nom, age, salaire):
        # Récupération de la vleur des paramètre de la classe
        self.nom = nom
        self.age = age
        self.salaire = salaire

    def afficher(self):
        """
        Permet d'affiché les paramètre en temps réel
        """

        print(
            f"Son nom c'est {self.nom}\n"+ 
            f"Il a {self.age} ans\n"+
            f"Il possède {self.salaire} euro de salaire"
            )

    def retrait(self, nombre:int) -> bool:
        """
        Permet de faire le retrait d'agent sur le salaire de la personne
        
        :   En cas d'erreur il doit envoyer **Vraie**
        """
        
        if isinstance(nombre, int): # renvoye une erreur sans arreter le programme
            print("Echec car la valeur demandé n'est pas valide")
            return 1

        if nombre < 0: # renvoye une erreur sans arreter le programme
            print("Echec car la demande n'est pas valide")
        
        if nombre > 62: # renvoye une erreur sans arreter le programme
            print("Echec car la demande dépasse le plafond")
            return 1

        self.salaire -= abs(nombre)
        return 0
        
