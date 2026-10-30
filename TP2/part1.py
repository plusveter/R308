



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




g = Grille()
g.afficher()
g.jouer(0, 0, "X")
g.afficher()
g.jouer(0, 1, "O")
g.afficher()
g.jouer(1, 1, "X")
g.afficher()


g.jouer(0, 0, "O") # -> refusé (occupée) 
g.afficher()
g.jouer(3, 0, "O") # -> refusé (hors grille)
g.afficher()
print(g.est_gagnant("X")) # -> False ; après 
g.jouer(2, 2, "X") # -> True
g.afficher()
print(g.est_plein())
print(g.est_gagnant("X"))