
a = b = "o"

while isinstance(a, str) and not a.isdecimal():
    a = input("Veuillez entrez le premier entier : ")
    
while isinstance(b, str) and not b.isdecimal():
    b = input("Veuillez entrez le second entier : ")

a, b = int(a), int(b)

print(
    f"Le plus petit des deux c'est : {(a if a < b else b)}" 
)

print(
    f"La somme des deux entier c'est : {sum(int(i) for i in range(a, b+1, (b-a) // abs((b-a)) ))}"
)

print(
    f"Le produit des deux est {("impaire" if (a + b)%2 != 0 else "paire") }"
)