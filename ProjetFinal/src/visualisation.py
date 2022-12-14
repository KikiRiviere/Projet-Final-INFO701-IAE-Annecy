from src.data import read_data_communes, read_data_aop
import wget
import os.path
import pandas as pd
import geopandas

# Exactement pareil que dans statistiques.py
def possibilites():
    choix_list = ["Afficher la carte des villes produisant du comté","Prendre une AOP par l’utilisateur et calculer la superficie totale des communes qui la produisent"]
    for i in range(0,len(choix_list)):
        print(str(i+1)," - ",str(choix_list[i]))

def villes_comte(): # Fonction qui liste toute les villes (dans le fichier .geojson) ayant l'AOP Comté
    commune = read_data_aop()[read_data_aop()["Aire géographique"] == "Comté"]
    com_pre = read_data_communes()[read_data_communes()["nom"].isin(commune["Commune"])] # N'Affiche que ceux qui sont dans le .geojson
    liste = com_pre.sort_values(by="code") # Trier par code postal
    liste.plot() # Ecriture de la carte
    print(liste)
    


def aop_superficie(): # Fonction pour calculer l'aire totale de production de chaque AOP
    choix_aop = str(input("Choississez un produit AOP (nom exacte avec majuscules et sans article) : "))
    commune = read_data_aop()[read_data_aop()["Aire géographique"] == choix_aop]
    com_pre = read_data_communes()[read_data_communes()["nom"].isin(commune["Commune"])]
    liste = com_pre.sort_values(by="code") # Trier par code postal
    surface = sum(liste["geometry"].length) # Fait la somme des aires
    surface = surface*100 # Met la surface en kilomètres carré
    print(liste)
    print("----\nLa surface de prodution de l'AOP " + choix_aop + " est d'approximativement " + format(surface, ".2f") + " kilomètres carrés dans la région AURA!\n----")


fonction_select = [villes_comte,aop_superficie]
