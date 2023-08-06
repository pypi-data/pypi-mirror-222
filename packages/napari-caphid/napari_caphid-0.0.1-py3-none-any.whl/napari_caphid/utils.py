import re
import os
from tqdm import tqdm
import matplotlib.pyplot as plt
from PIL import Image



def replace_pixel(current_array):
    current_array[current_array==0]=1 # winged adult
    current_array[current_array==51]=2 # apterous adult
    current_array[current_array==102]=3 # nymph
    current_array[current_array==153]=4 # larvae
    current_array[current_array==204]=5 # nymph-larvae small
    current_array[current_array==255]=6 # molt
    current_array[current_array==205]=0 # fond
    return current_array

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

def detect_country_f(dico_pays,un_string):
    # Obtenir le nom pays en prenant en compte les majuscules et les minuscules
    for ix in dico_pays.keys():
        if un_string.find(ix)!=-1:
            return ix
        
def chemin_image_dossier(chemin_country):
    # Obtenir le nom image du dossier country en prenant en compte les majuscules et les minuscules
    for ix in os.listdir(chemin_country):
        if os.path.isdir(os.path.join(chemin_country,ix)) and ix.lower()=="image":
            return ix

def nom_des_images_image_dossier(total_path_dossier_image):
    # Obtenir le nom des images contenu dans image du dossier country par ordre alphabetique
    print("Path",total_path_dossier_image)
    A = []
    for ix in os.listdir(total_path_dossier_image):
        A.append(ix)
    dirlist = sorted_alphanumeric(A)
    return dirlist