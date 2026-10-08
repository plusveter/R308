from exo7 import *


class Employe(Personne):
    def __init__(self, nom, age, salaire, prime):
        super().__init__(nom, age, salaire)
        self.prime = prime

    def afficher(self):
        super().afficher()

        print((
            "Il est à son prime"
            if self.prime else
            "Il n'est pas à son prime"
            ))


if __name__ == "__main__":
    Employe("Sonic", 10, 50, 0).afficher()