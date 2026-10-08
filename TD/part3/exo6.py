data:dict[str] = {}

for i in range(3):
    # Affichage du compteur
    print(f"\n [PERSONNE N°{i}]")

    # Récupération du nom de la personne
    nom = input("Veuillez entrez un nom de famille:") 

    # Récupération du numéro de téléphone
    tel = ""
    # Cette boucle permet d'évité les erreur de convertion quand on fait STR à INT
    while isinstance(tel, str) and (not tel.isdecimal() or len(tel) != 10):
        tel = input("Veuillez entrez un numéro de téléphone valide  :")

        if not tel.isdecimal(): print('Il doit avoir des chiffre seulement')
        elif (len(tel) != 10): print(f"Il doit avoir 10 chiffre au lieu de {len(tel)}")
    tel = int(tel)

    # Ajout des donnée de la personne dans la base de donnée
    data[nom] = tel

# Affiche la version actuelle de la base donnée de base
print('\n') # saut de ligne avant l'affichage
for nom in data : print(f"Le numéro de téléphone de {(nom.upper())} c'est {data[nom]}")
print('\n') # saut de ligne après l'affichage


# Récupère le nom le plus long
name = max(data.keys())

# Modification du numéro de téléphone de la personne avec le nom le plus long
tel = ""
while isinstance(tel, str) and (not tel.isdecimal() or len(tel) != 10): # Cette boucle permet d'évité les erreur de convertion quand on fait STR à INT
    tel = input(f"Veuillez modifier le numéro de téléphone de {name} :")

    if not tel.isdecimal(): print('Il doit avoir des chiffre seulement')
    elif (len(tel) != 10): print(f"Il doit avoir 10 chiffre au lieu de {len(tel)}")
data[name] = int(tel)

# Supression d'un entré dans la list
data.pop(sorted(data.keys())[-2])

# Affiche la nouvelle version de la base donnée de base

print('\n') # saut de ligne avant l'affichage
print("La nouvelle version de la base de donnée.")
for nom in data : print(f"Le numéro de téléphone de {(nom.upper())} c'est {data[nom]}")
print('\n') # saut de ligne après l'affichage





