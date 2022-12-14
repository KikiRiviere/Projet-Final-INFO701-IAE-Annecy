from src.data import read_data_communes, read_data_aop
import wget
import os.path

import pandas as pd
import geopandas

# Fonction regroupent les informations des fonctions disponibles
def possibilites():
    choix_list = ["Fonction de Test","Prendre un nom de commune de l’utilisateur et afficher toutes les informations stockées dans le tableau AOP relatif à cette commune","Afficher la liste des noms de communes sans doublons","Afficher la liste des AOPs sans doublons","Prendre un nom d’AOP et afficher toutes les communes qui le produisent","Afficher le nombre d’AOP par commune pour toutes les communes","Afficher le nombre de communes par AOP pour les AOP","Afficher tous les AOP entre deux codes-postaux en demandant le min code postal et max code postal à l’utilisateur"]
    print('Voici la liste des options que vous pouvez prendre :')
    for i in range(0,len(choix_list)): # Création du menu d'options
        print(str(i+1)," - ",str(choix_list[i]))

# Liée à la fonction de base.
main_list = [read_data_aop,read_data_communes]

def base(): # Fonction pour montrer le AOP ou les COMMUNES
    choix = int(input("Veuillez faire un choix ! (1 = AOP / 2 = COMMUNES) : "))
    if choix == 1 :
        print(main_list[0]())
        
    elif choix == 2 :
        print(main_list[1]())
    else:
        print("Une erreur est survenu !")

def commune_aop(): # Fonction pour montrer les infos d'une commune dans les deux fichiers
    choix_communes = str(input("Choississez une commune (sans article) : ")) # Choix de la commune
    # Fichier .csv
    commune = read_data_aop()[read_data_aop()["Commune"] == choix_communes]
    print(commune.head())
    # Fichier .geojson
    com_pre = read_data_communes()[read_data_communes()["nom"] == choix_communes] 
    print(com_pre)
    
def group_communes(): # Fonction pour montrer toutes les communes
    resultat = read_data_aop().groupby("Commune")["CI"].nunique()
    print(resultat)
    
def group_aop(): # Fonction pour montrer toutes les AOP
    resultat = read_data_aop().groupby("Aire géographique")["Aire géographique"].nunique()
    print(resultat)
    
def commune_prod_aop(): # Fonction pour un AOP avoir toutes les communes
    choix_aop = str(input("Choississez un produit AOP (sans article) : ")) # Choix de l'AOP
    prod_aop = read_data_aop()[read_data_aop()["Aire géographique"] == choix_aop] # Prendre que ceux qui ont l'AOP
    print(prod_aop)
    
def nb_aop_communes(): # Fonction pour le classement des communes en nombre d'AOP
    print("Voici le classement du nombre d'AOP par commune :")
    resultat = read_data_aop()["Commune"].value_counts() # Remplace un =COUNT dans un Excel
    print(resultat)
    
def nb_communes_aop(): # Fonction pour le classement des AOP en nombre de communes producteurs
    print("Voici le classement du nombre de communes par AOP :")
    resultat = read_data_aop()["Aire géographique"].value_counts() # Remplace un =COUNT dans un Excel
    print(resultat)
    
def entre_deux_CP(): # Fonction qui montre la liste de commune entre deux code postales
    cp1 = input("Choix du plus petit code postal demandé : (5 chiffres obligatoires) ") # Choix du minimum
    cp2 = input("Choix du plus grand code postal demandé : (5 chiffres obligatoires) ") # Choix du maximum
    
    liste = read_data_aop().sort_values(by="CI") # Met dans l'ordre les CP dans le fichier .csv
    resultatbis = liste[liste["CI"].between(cp1,cp2)] #  Affiche la liste

    print(resultatbis)
        
# Liste de selection de la fonction
fonction_select = [base,commune_aop,group_communes,group_aop, commune_prod_aop,nb_aop_communes,nb_communes_aop,entre_deux_CP]
