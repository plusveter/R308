import random



class Grille():
    def __init__(self):
        self.data = [ [" ", " ", " "], [" ", " ", " "], [" ", " ", " "] ]
        self.longueur = 3
        self.largeur = 3

    def est_plein(self):
        remplie = True
        for y in range(self.largeur):
            for x in range(self.longueur):
                remplie = remplie and self.data[y][x] == " "
        return remplie
    
    def est_gagnant(self, char):
        for y in range(self.largeur):
            line = ""
            for x in range(self.longueur):
                if self.data[y][x] == char:
                    line += char
            if len(line) >= 3:
                return True

        for y in range(self.longueur):
            colone = ""
            for x in range(self.largeur):
                if self.data[y][x] == char:
                    colone += char
            if len(colone) >= 3:
                return True

        diag = ""
        for i in range(3):
            if self.data[i][i] == char: 
                diag += char
        if len(diag) >= 3:
            return True

        rdiag = ""
        for i_ in range(3):
            i = 2-i_
            if self.data[i][i] == char: 
                rdiag += char
        if len(rdiag) >= 3:
            return True

        return False

    def jouer(self, x, y, char):


        if  (x < 0 or x >= 3) or (y >= 3 or y < 0): 
            print("refusé (hors grille)")
            return False
        
        if self.data[y][x] != ' ': 
            print("refusé (occupée) ")
            return False
        
        self.data[y][x] = char
        return True
        
        

    def afficher(self):
        print(" ")
        for y in range(self.largeur):
            line = ""
            for x in range(self.longueur): 
                line += self.data[y][x]
                if x < 2 : 
                    line += " | "
            
            print(line)
            print("-"*3*3)
        print(" ")


class JoueurAI:
    def __init__(self):
        pass

    def play(self):
        while not grille.jouer(random.randint(0, 2), random.randint(0, 2), "A"): ...
            

class Joueur:
    def demande_int(self, prompt:str) -> int:
        """
        demande_int c'est une fonction qui permet de faire la demande d'entier positif à l'utilisateur
        """
        
        if not isinstance(prompt, str): 
            raise TypeError("La variable prompt n'est pas sous le format string")
        
        a = str()
        
        # Vérifie si c'est une variable string & si elle peut être converti en entier
        while isinstance(a, str) and (not a.isdecimal()): 
            a = input(prompt)
            if not a.isdecimal(): print("Seulement les entier positif sont autorisé.\n") 

        return int(a) # Renvoie la version entier de la chaine de caractère


def main():
    pass

if __name__ == "__main__":
    grille = Grille
    main()
