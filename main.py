# -*- coding: utf-8 -*-
"""
Created on Wed May 11 20:02:06 2022

@author: Tabrose HOSSAIN
"""

import otsu
import multiotsu
import hysteresis
import contours
import numpy as np
from PIL import Image
import os

from tkinter import Tk
from tkinter.filedialog import askopenfilename

def full_method_multiotsu(img, L=256, M=32):
    hist = otsu.calcul_hist(img)
    thresholds = multiotsu.Multithreshold_Otsu(hist, M=M, L=L)
    return thresholds

def full_method_otsu(img):
    hist = otsu.calcul_hist(img)
    threshold = multiotsu.otsu_threshold_value(hist)
    return threshold

def full_hysteresis(image, threshold, value):
    y = hysteresis.hysteresis_threshold(image, threshold)
    y = hysteresis.hysteresis(y, value)
    return y

def main():
    #path = 'img_ori/'
    #file = '516-8-3_fr2-006.tif'
    
    Tk().withdraw()
    filename = askopenfilename()
    file = filename[-19:]
    
    #tif = Image.open(path+file)
    tif = Image.open(filename)
    tif = np.array(tif)
    #img = Image.open(path+file).convert('L')
    img = Image.open(filename).convert('L')
    img = np.array(img)
    
    otsu_threshold = full_method_otsu(img)
    multiotsu_thresholds = full_method_multiotsu(img, L=256, M=32)
    multiotsu_thresholds.append(otsu_threshold)
    
    optimal_threshold_value = min(multiotsu_thresholds)
    #optimal_threshold_value = otsu_threshold
    
    threshold_image = full_hysteresis(img, optimal_threshold_value, 127)
    
    if not os.path.exists('img_mask'):
        os.makedirs('img_mask')
    
    mask = Image.fromarray(threshold_image)
    mask = mask.convert('RGB')
    mask.save(f"img_mask/mask_{file}")
    
    mask_path = 'img_mask/'
    mask_file = f'mask_{file}'
    
    row, col, chan = tif.shape
    background = int(img.mean())

    for i in range(row):
          for j in range(col):
              if threshold_image[i][j] != 255:
                  for k in range(chan):
                      tif[i][j][k] = background
                      
    if not os.path.exists('img_res'):
        os.makedirs('img_res')

    image_threshold = Image.fromarray(tif)
    image_threshold = image_threshold.convert('RGB')
    image_threshold.save(f"img_res/rgb_{file}")
    
    res_path = 'img_res/'
    res_file = f'rgb_{file}'
    
    contours.find_contours(mask_path, mask_file, res_path, res_file, file)


if __name__ == '__main__':
    main()
