# Ecriture des questions et des réponses
question = ["Combien de communes produisent l'AOP Livarot?","Combien d'AOP possède le commune d'Abondance?","Quelle est la commune avec le plus d'AOP?","Combien d'AOP possède la totalité des communes de l'Ain?","Lyon possède-t-il des AOP? (Oui/Non)","L'AOP Bleu d'Auvergne est produit dans PLUS ou MOINS de communes que l'AOP Bleu du Vercors-Sassenage? (Plus/Moins)","Dans combien de communes, l'AOP Comté est-il produit?","L'AOP Reblochon de Savoie peut-il être produit dans PLUS ou MOINS de 3500 kilomètres carré? (Plus/Moins)","Combien y'a t-il d'AOP en France?","Thonon-les-Bains possède t-il l'AOP Vin de Savoie? (Oui/Non)","L'AOP Morbier peut-t-il être produit dans PLUS ou MOINS de 1500 kilomètres carré? (Plus/Moins)","Grenoble possède t-il l'AOP Noix de Grenoble? (Oui/Non)"]
reponse = ["2097","3","Saint-Hippolyte","901","Non","Plus","211","Plus","1430","Oui","Moins","Oui"]

# Entrée du pseudo (utilisé avant chaque question)
pseudo = input("Ecrivez un pseudo avant de commencer le prossessus : ").title()

def debut(): # Signe du début du quizz
    print("-- Début du Quiz --\n\n")
        
    
def quizz(): 
    # Définition du nombre de vies et de points à la base
    points = 0
    vies = 3
    
    # Boucle pour le déroulé du quizz
    for i in range(0,len(question)):
        print("\n---- \nProchaine question, " + str(pseudo) + " !\n---")
        
        print("Voici la question numéro " + str(i+1) + ":")
        print(question[i])
        reponse_donnee = input("Votre réponse? : ")
        if reponse_donnee == reponse[i]: # Réponse juste ou réponse fausse ?
            points +=1
            print("\n----\nBonne réponse ! :D\n----")
        else:
            print("\n----\nMauvaise réponse ! :/\n----")
            vies = vies - 1 
            if vies == 0: # Si les vies atteignent 0 = perdu
                print()
                print("\n----\nVous avez perdu ! >:(\n----")
                break
            
        if points == 10: # Si 10 points = gagné
            print("\n----\nVous avez gagné ! :D\n----")
            break
            
        print("\n\n----\nIl vous reste " + str(vies) + " vies !\n----")
        print("\n----\nVous avez " + str(points) + " points !\n----")


                      
      