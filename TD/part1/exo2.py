
a = ""

while isinstance(a, str) and not a.isdecimal():
    a = input("Veuillez entrez un entier : ")

print(
    sum(i for i in range(int(a)+1))
)