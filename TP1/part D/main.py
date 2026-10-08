from deadman import hangman
import random, os

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
    # Renvoie un mot en majuscule
    # grace à la section de liste via la fonction randint de random
    # qui est définit entre 0 et la taille de la liste
    return (listes[random.randint(0, len(listes)-1)]).upper()

mot = choisir_mot(charger_list("./list.txt"))

# Utile récupéré le nombre de tentative
tentative = 7 

# Récupère les lettre unique
lettres = [] 

# List de caractère interdit dans le jeu
black_list = [
    "!", '"', "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/",
    ":", ";", "<", "=", ">", "?", "@",
    "[", "\\", "]", "^", "_", "`",
    "{", "|", "}", "~"
]

print("Jeu d'essai")
while tentative > 0: # Boucle qui vérifie le nombre de tentative
    masque = "" # variable string qui contient rien
    for i in mot:  # Boucle qui lit le mot lettre par lettre
        # Condition qui vérifie si la lettre exist pour l'ajouté dans l'affichage du masque
        # Dans le cas ou il n'est pas, il renvoie ce caractère "_"
        masque += i+' ' if i.lower() in lettres else "_ " 

    if masque.replace(' ', '').lower() == mot.lower(): # Vérifie si les mots sont 
        print(f"{mot.upper()}, saisies {masque.upper()} -> Gagné")
        break # Casse la boucle de force pour finir le jeu

    print(f"""{masque.upper()}""") # Affichage des mots restand

    # On définit une vairiable pour la boucle ci-dessous
    char_demande = "" 
    # La boucle continue tants que la variable n'a pas un 1 seul caractère
    # ou si la lettre exist déjà
    # ou si la lettre est mentionné dans le black list
    while len(char_demande) != 1 or (char_demande in lettres) or (char_demande in black_list):
        # Demande à l'utilisateur une lettre
        char_demande = input("Veuillez entré une lettre : ")

        if (len(char_demande) != 1): # Vérification de la taille de la chaine de caractère 
            print(F"Vous avez saisie plus d'un caractère :{char_demande}")
            continue # force le saut vers le début (un peu comme un JUMPTO en assembly)

        if (char_demande in black_list): # Vérification si c'est autorisé
            print(f"{char_demande} n'est pas autorisé")
            continue # force le saut vers le début (un peu comme un JUMPTO en assembly)

        if (char_demande in lettres): # Vérification si il existe déjà
            print(f'Vous avez déjà saisi ce caractère : {char_demande}\n')
            continue # force le saut vers le début (un peu comme un JUMPTO en assembly)

        lettres.append(char_demande.lower()) # Enregistre la lettre

        break # Casse la boucle, nécessaire pour évité une boucle infinit 

    if char_demande.lower() in mot.lower(): ... # Ne fait rien, exist seulement pour la condition opposé
    else:
        tentative -= 1 # Retire une tentive 
        print(f"La lettre {char_demande} n'est pas dans le mot\n") # 

        print(hangman[tentative]) # Affiche le pendu

        if tentative > 0: print(f"Il vous reste {tentative} tentative.") # Affiche le nombre de tentative tant que la tentative est superieur à 0 

    # Vérifie si il y a encore des tentatives
    if tentative <= 0: print(f"sept lettres fausses -> Perdu, le mot était {mot.upper()}") # fin de la boucle
        