# -*- coding: utf-8 -*-
"""
Created on Wed May 11 20:02:06 2022

@author: Tabrose HOSSAIN
"""

import cv2
from PIL import Image
import os
import numpy as np


def find_contours(mask_path, mask_file, res_path, res_file, file):
    img = cv2.imread(mask_path+mask_file)
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    img_color = Image.open(res_path+res_file)
    
    if not os.path.exists('single_sediment'):
        os.makedirs('single_sediment')
    
    if not os.path.exists(f'single_sediment/{file[:15]}'):
        os.makedirs(f'single_sediment/{file[:15]}')
    
    contours = cv2.findContours(img_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]
    for i, cntr in enumerate(contours):
        x,y,w,h = cv2.boundingRect(cntr)
        if w > 20 or h > 20:
            box = (x-10, y-10, x+w+10, y+h+10)
            area = img_color.crop(box)
            area_array = np.array(area)
            shape = area_array.shape
            width = shape[0]-1
            height = shape[1]-1
            if area_array[0][0][0] != 0 and area_array[width][0][0] != 0 and area_array[0][height][0] != 0 and area_array[width][height][0] != 0:
                area.save(f"single_sediment/{file[:15]}/{res_file[:15]}_{i}.tif")
