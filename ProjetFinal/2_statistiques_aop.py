from src.statistiques import fonction_select,possibilites


# Affichage de la boîte d'option pour exécuter les fonctions
print("----\nBienvenue dans l'exploreur d'option !\n----")

possibilites() # Activation de la boîte de dialogue pour la 1ère fois
choix_fonction = int(input("Choississez une fonction à mettre en avant : ")) # Choix de la fonction
fonction_select[choix_fonction-1]() # Recherche de la fonction désiré dans une liste située dans statistiques.py
while True : # Boucle de possibilites() tant que on dit Oui.
    print("\n----\nVoulez-vous voir une autre fonction ? (Oui/Non)\n----")
    yes = input("> ")
    if yes == "Oui" or yes == "oui":
        possibilites()
        choix_fonction = int(input("Choississez une fonction à mettre en avant : "))
        fonction_select[choix_fonction-1]()
    else :
        print("\n----\nAu revoir !\n----")
        break
