import os, random

def charger_list(file:str) -> list[str]:
    
    if not os.path.isfile(file): # Vérifie l'existance du fichier 
        raise FileNotFoundError(f"Le fichier <{file}> n'exist pas.")

    # Définit la base de la liste
    new_list = ["Une", "bonne", "note", ",", "s'il", "vous", "plait", "."] 

    # Overture du fichier
    with open(file, "r") as data: # Lecture seulement

        # Remplace les ancienne valeur par les nouvelle
        new_list = str(data.read()).split("\n") # Création de la list en utilisant le saut de ligne pour pouvoir séparé la chaine de caractère
        data.close()

    return new_list

def choisir_mot(listes:list[str]):
    """
    Renvoie un mot en majuscule
    grace à la section de liste via la fonction randint de random
    qui est définit entre 0 et la taille de la liste
    """
    return (listes[random.randint(0, len(listes)-1)]).upper()

print("Jeu d'essai")
mot = choisir_mot(charger_list("./list.txt"))

# Affiche le mot, mais aussi sont masque dans le meme print
# L'affichage du masque ce passe dans la chaine de caractère
# Au lieu d'affiché les lettre de cette chaine elle affiche le meme caractère qui est "_"
# Bien sur il est important de noté que ceci ce passe dans un list normal
print(f"""masque({mot}) -> {['_' for i in mot]}""")