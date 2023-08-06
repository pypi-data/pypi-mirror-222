"""
This module is an example of a barebones QWidget plugin for napari

It implements the Widget specification.
see: https://napari.org/stable/plugins/guides.html?#widgets

Replace code below according to your needs.
"""
from typing import TYPE_CHECKING

from magicgui import magic_factory
from qtpy.QtWidgets import QHBoxLayout, QPushButton, QWidget

import os
from tqdm import tqdm
from PIL import Image
from skimage.io import imread
import numpy as np
import cv2
import pandas as pd
import pathlib

from napari_caphid.utils import *
from napari.types import ImageData, LabelsData

if TYPE_CHECKING:
    import napari
    
    
dico_aphids_label = {
  1:"winged adult",
  2:"apterous adult",
  3:"nymph",
  4:"larvae",
  5:"nymph-larvae small",
  6:"molt",
}
        
def process_image(A,current_array_new,dico_pays,country_det):
    class_dataset_ = []
    surface_dataset_ = []
    name_dataset_ = []
    class_inf = []

    for ids in tqdm(range(len(A)),desc=f"{country_det}"):
        arr_ = current_array_new[ids,...].astype('uint8')
        contours,hierarchy = cv2.findContours(arr_,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        
        for i, cnt in enumerate(contours):
                
            mask = np.zeros((arr_.shape[0],arr_.shape[1]), np.uint8)
            newnew_ = cv2.fillPoly(mask, pts = [cnt], color=(255,255,255))
            new_new_new_ = np.where(newnew_!=0,arr_,0)
            or_zero = np.unique(new_new_new_)
            labels_detec_ = or_zero[or_zero!=0][0]
                
            M = cv2.moments(cnt) 
            area = cv2.contourArea(cnt)
            
            mask = np.zeros((arr_.shape[0],arr_.shape[1]), np.uint8)
            newnew_ = cv2.fillPoly(mask, pts = [cnt], color=(255,255,255))
            new_new_new_ = np.where(newnew_!=0,arr_,0)
            or_zero = np.unique(new_new_new_)
            labels_detec_ = or_zero[or_zero!=0][0]
            
            class_inf.append([dico_aphids_label[labels_detec_],area])

        my_class_ = [class_inf[ix][0] for ix in range(len(class_inf))]
        my_surface_ = [class_inf[ix][1] for ix in range(len(class_inf))]
        my_name_ = [A[ids]]*len(my_surface_)
        
        class_dataset_=class_dataset_+my_class_
        surface_dataset_=surface_dataset_+my_surface_
        name_dataset_=name_dataset_+my_name_

    name_dataset_updt =  []
    for il in range(len(name_dataset_)):
        head,_ = os.path.splitext(name_dataset_[il])
        name_dataset_updt.append(head)

    country_dataset_current_ = [dico_pays[country_det]]*len(name_dataset_updt)
    df_new = pd.DataFrame({"Country":country_dataset_current_,"Image":name_dataset_updt,"Class":class_dataset_,"Surface (pxl)":surface_dataset_})
    df_new["Surface (µm)"] = df_new["Surface (pxl)"]*4.84
    return df_new

def update_table_csv(df_new,country_det,path_to_outlier,current_raw_table_df):
    image_traiter_list_ = list(np.unique(np.array(df_new["Image"])))
    print("Image processed:",len(image_traiter_list_))
    for idx_nom_image in tqdm(range(len(image_traiter_list_)),desc="Update table"):
        mon_image = image_traiter_list_[idx_nom_image]
        df_new_subset_current = df_new.loc[df_new["Image"]==mon_image]

        idx_to_drop = current_raw_table_df.loc[((current_raw_table_df["Country"].map(str.lower)==country_det) & (current_raw_table_df["Image"]==mon_image))].index
        current_raw_table_df = current_raw_table_df.drop(idx_to_drop)
        current_raw_table_df = pd.concat([current_raw_table_df,df_new_subset_current], ignore_index=True)

        current_raw_table_df.loc[((current_raw_table_df["Country"].map(str.lower)==country_det) & (current_raw_table_df["Image"]==mon_image))]
    # HERE PATH 
    # current_raw_table_df.to_csv(r'D:\BACKUP_DESKTOP_E6U3VO4\User\Aphid\outlier\table_raw\Aphid_output.csv',index=False)
    # current_raw_table_df.to_csv(path_to_raw_table_,index=False)
    current_raw_table_df.to_csv(os.path.join(path_to_outlier,"output_dataframe.csv"),index=False)
    

@magic_factory(Country_={"choices": ['france', 'belgium', 'spain','']},
               path_to_raw_table_={"label": "Pick a table:"})
def process_func(Mask_: LabelsData,path_to_raw_table_=pathlib.Path.cwd(),Country_=''):
    #path_to_raw_table_ = r"D:\BACKUP_DESKTOP_E6U3VO4\User\Aphid\outlier\Aphid.csv"
    
    #I)
    #Importer tableau Aphid.csv
    # HERE PATH 
    # path_to_raw_table = r"D:\BACKUP_DESKTOP_E6U3VO4\User\Aphid\outlier\table_raw"
    # current_raw_table_df = pd.read_csv(os.path.join(path_to_raw_table,'Aphid.csv'))
    path_to_outlier = os.path.dirname(path_to_raw_table_)
    current_raw_table_df = pd.read_csv(path_to_raw_table_)

    #II)
    #Stack image et pays
    dico_pays = {"spain":"Spain","france":"France","belgium":"Belgium"}
    # HERE PATH 
    # path_to_outlier = r"D:\BACKUP_DESKTOP_E6U3VO4\User\Aphid\outlier"
    # stack_images_files = [ix for ix in os.listdir(path_to_outlier) if ix.find('correction')!=-1] #list of name of stack file
    
    # print("Stack image",stack_images_files[ix],'<',os.path.join(path_to_outlier,stack_images_files[ix]),'>')
    # country_det = detect_country_f(dico_pays,stack_images_files[ix])
    country_det = Country_
    print("Country",country_det)
    chemin_country = os.path.join(path_to_outlier,dico_pays[country_det])
    
    #Retrouver le nom des images
    nom_dossier_image = chemin_image_dossier(chemin_country)
    total_path_dossier_image = os.path.join(chemin_country,nom_dossier_image)
    A = nom_des_images_image_dossier(total_path_dossier_image)
    
    # current_array = imread(os.path.join(path_to_outlier,stack_images_files[ix]))
    current_array = Mask_
    current_array_cp = np.copy(current_array)

    if country_det=="france":
        current_array_new = np.copy(current_array_cp)
    else:
        current_array_new = replace_pixel(current_array_cp)
    
    df_new = process_image(A,current_array_new,dico_pays,country_det)
    # update_table_csv(df_new,country_det,path_to_raw_table_,current_raw_table_df)
    update_table_csv(df_new,country_det,path_to_outlier,current_raw_table_df)
