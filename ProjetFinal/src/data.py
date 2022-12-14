'''
File: data.py
Created Date: Wed Oct 26 2022
Author: Ammar Mian
-----
Last Modified: Thu Nov 17 2022
Modified By: Ammar Mian
-----
Copyright (c) 2022 Université Savoie Mont-Blanc
-----
'''

import wget
import os.path
import pandas as pd
import geopandas



def download_data(url, destination, filename):
    """Télécharger une donnée sur internet à partir d'une url et l'enregistrer à l'emplacement
    voulu

    Parameters
    ----------
    url : str
        url du fichier à télécharger
    destination : str
        dossier où télécharger le fichier
    filename : str
        nom du fichier sauvegardé
    """

    file_path = os.path.join(destination, filename)

    # Vérifier que la donnée n'existe pas avant de télécharger
    if not os.path.exists(file_path):
        print(f"Downloading data from {url} into {file_path}")
        wget.download(url, file_path)
    else:
        print(f"File {file_path} already exists!")

def read_data_aop(): # Lecture du fichier .csv (avec l'extension pandas)
    return pd.read_csv("./data/aop.csv",dtype=object,sep=";",on_bad_lines='error',encoding='iso8859_15')


def read_data_communes(): # Lecture du fichier .geojson et création d'une map (avec l'extension geopandas)
    return geopandas.read_file("./data/communes_aires.geojson")
