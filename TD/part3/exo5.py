list = []

for i in range(5):
    a = ""

    while ( 
            isinstance(a, str) #        Vérifie si la variable est un string
            and not a.isdecimal() #     Vérifie si le string peut être convertie en entier
        ):
        a = input(f"Veuillez saisir l'entier n°{i} : ") # Fait la demande de l'entier auprès de l'utilisateur
    
    a = int(a) #                        Reconvertie à la fin de la bouble 
    print(a)
    list.append(a) #                    Rajoute cette entier à la liste

print(
    f"La liste de base c'est : {list}"
)#                                      Affiche la liste originelle

print(
    min(list)
) #                                     Affiche la valeur minimum dans la liste

print(
    max(list)
) #                                     Affiche la valeur maximum dans la liste

print(
    ( sum(list)/5 )
) #                                     Affiche la valeur moyenne de cette list

new_list = sorted(list) #               Création d'une variable copie de liste, mais celle-ci est triée
print(
    f"La liste triée : {new_list}"
) #                                     Affichage de cette nouvelle liste