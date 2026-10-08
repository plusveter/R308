# Création d'un nouveau dictionnaire étudiant
etudiant:dict = {}

def ajouter_etudiant(d:dict, nom:str, note:float):

    ### Vérification que c'est bien un dictionnaire
    if not isinstance(d, dict):
        raise TypeError("La variable d n'est pas un dictionnaire")

    ### Vérification du nnom
    if not isinstance(nom, str): # Check si c'est un string
        raise TypeError(f"Le nom donnée <{nom}> n'est pas une chaine de caractère")

    if len(nom) < 3:
        raise Exception(f"Le nom donnée <{nom}> possède {len(nom)} charactère")

    ### Vérification de la note
    if isinstance(note, int): pass # Vérifie si c'est un entier
    elif not isinstance(note, float): # Check si c'est un float
            raise TypeError(f"La note attribué pour '{nom}' n'est pas un float : <{note}>")

    if not (0 < note <= 20): # Vérifie si le contenu des variables est correct
        
        # Création d'une condition de simple à l'interieur de la chaine de charactère qui donne une réponse different en fonction de la note donnée
        raise Exception(f"""La note attribué pour '{nom}' est {
            ("superieur à 20" if note > 20 else "inferieur à 0") 
            } : {note} """) 
    
    d[nom] = note

def moyenne_classes(d) -> float:
    ### Vérification que c'est bien un dictionnaire
    if not isinstance(d, dict):
        raise TypeError("La variable d n'est pas un dictionnaire")
    
    # Fait incrémente dans une list via une boucle à l'interieur, les note des étudiants
    # puis fait la somme de cette meme liste 
    # puis divise cette some par la taille de la list
    # puis arrondie par 2 le résultat 
    return round(sum([d[nom] for nom in d])/len(d), 2)

def meilleur_etudiant(d) -> tuple:
    ### Vérification que c'est bien un dictionnaire
    if not isinstance(d, dict):
        raise TypeError("La variable d n'est pas un dictionnaire")
    
    # Rajoute de la variable local meilleurs notes
    meilleur:tuple = "Aucun", 0

    # Boucle qui va permetre de trouvé la meilleur notes
    for nom, note in d.items(): # Extraction des donnés nom & étudiant
        _, meilleur_note = meilleur

        if note < meilleur_note:
            continue # Fait un saut dans la liste

        # Remplace le nom actuelle de l'étudiant
        meilleur = nom, float(note)

    # Renvoie le tuple
    return meilleur

def sauvegarde_etudiant(d:dict):
    ### Vérification que c'est bien un dictionnaire
    if not isinstance(d, dict):
        raise TypeError("La variable d n'est pas un dictionnaire")
    
    with open("list.json", "w+") as file: # Créer un nouveau fichier (au lieu de concaténé)
        chaine_de_caractère = str(d) # Converti le dictionnaire en chaine de caractère
        chaine_de_caractère = chaine_de_caractère.replace("'", '"') # Replace les ' par " pour une meilleur compatibilité
        file.write(chaine_de_caractère) # Ecrit dans le fichier
        file.close() # Ferme l'écriture du fichier

print("Jeu d'essai")

ajouter_etudiant(etudiant, "Alice", 12)
ajouter_etudiant(etudiant, "Bob", 15)
ajouter_etudiant(etudiant, "Claire", 9.5)

### Affichage de la list des étudiant en brute

# Je génère une chaine de caractère dans une list dans une chaine de caractère
list_etudiant = f"{[f'{nom} {etudiant[nom]}' for nom in etudiant]}"

# J'applique un filtre pour retiré dans cette chaine les caractère suivant : '[]
list_etudiant = list_etudiant.replace("'", "").replace("[", "").replace("]", "")

#J'affiche la list dans la console
print(list_etudiant)


### Affichage de la moyenne
print("moyenne_classe(d) -> ", moyenne_classes(etudiant))
print("meilleur_etudiant(d) -> ", meilleur_etudiant(etudiant))
sauvegarde_etudiant(etudiant)
        