import random # Import de la lib random

nombre = random.randint(0, 100) # fait le demande d'un nombre entre 0 à 100

def demande_int(prompt:str) -> int:
    """
    demande_int c'est une fonction qui permet de faire la demande d'entier positif à l'utilisateur
    """
    
    if not isinstance(prompt, str): # Renvoie une erreur dans le cas ou le string n'as pas le bon format
        raise TypeError("La variable prompt n'est pas sous le format string")
    
    # Créer une variable string
    a = "" 
    while isinstance(a, str) and (not a.isdecimal()): # Vérifie si c'est une variable string & si elle peut être converti en entier
        a = input(prompt) # Fait la demande à l'utilisateur

        # Gestion d'erreur interne 
        if not a.isdecimal(): print("Seulement les entier positif sont autorisé.\n") 

    return int(a) # Renvoie la version entier de la chaine de caractère


result = -1 
while result != nombre:
    result = demande_int("Veuillez entré un nombre entre 0 à 100 : ") # Fait le demande d'un entier avec un prompt

    if result == nombre: print("Gagné")  # Fin

    elif result < nombre: print("Trop petit") # Indication
    else: print("Trop grand") # Indication
    
