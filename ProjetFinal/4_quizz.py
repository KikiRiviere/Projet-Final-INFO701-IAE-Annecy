from src.quizz import quizz,debut


# Fonction de lancement du quizz
def lancement():
    print("\n----\nBonjour et bienvenue dans le possessus de quiz !\n----")
    yes = input("Voulez-vous commencer un quiz avec nous ? (Oui/Non) : ")
    if yes == "Oui" or yes == "oui" :
        print("Bonne chance ! \n\n")
        debut()
        quizz()
        while True : # Boucle si on veut refaire le quizz.
            ja = input("Voulez-vous recommencer ? (Oui/Non) : ")
            if ja == "Oui" or ja == "oui":
                quizz()
            else:
                print("\n----\nAu revoir !\n----")
                break
    else :
        print("\n----\nTant pis...\n----")
                
lancement()
            
            

