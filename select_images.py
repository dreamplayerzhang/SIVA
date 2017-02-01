# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 17:48:22 2017

@author: josemiguelarrieta
"""
#Load libraries
import os 
os.chdir('Documents/SIVA')
from utils_dagm import save_list_selected_images, load_list_selected_images, move_selected_images,select_images

#####################################
#Select Images For Experiment dagm# #
#####################################
class_number = 4
number_experimet = 1


list_no_defect = select_images('',class_number)
list_defect_A = select_images('A',class_number)
list_defect_AB = select_images('AB',class_number)
list_defect_B = select_images('B',class_number)

save_list_selected_images(list_no_defect,'',class_number,number_experimet)
save_list_selected_images(list_defect_A,'A',class_number,number_experimet)
save_list_selected_images(list_defect_B,'B',class_number,number_experimet)
save_list_selected_images(list_defect_AB,'AB',class_number,number_experimet)

A = load_list_selected_images('',class_number,number_experimet)
B = load_list_selected_images('A',class_number,number_experimet)
C = load_list_selected_images('B',class_number,number_experimet)
D = load_list_selected_images('AB',class_number,number_experimet)

move_selected_images(list_no_defect,'',class_number,number_experimet)
move_selected_images(list_defect_A,'A',class_number,number_experimet)
move_selected_images(list_defect_AB,'AB',class_number,number_experimet)
move_selected_images(list_defect_B,'B',class_number,number_experimet)



