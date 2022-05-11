# -*- coding: utf-8 -*-
"""
Created on Wed May 11 20:02:06 2022

@author: Tabrose HOSSAIN
"""

import numpy as np


def hysteresis_threshold(img, threshold):
    high = threshold
    low = 0.45 * threshold
    row, col = img.shape
    y = np.zeros((row, col))
    for i in range(row):
        for j in range(col):
            if img[i][j] >= high:
                y[i][j] = 255
            elif img[i][j] <= low:
                y[i][j] = 0
            else:
                y[i][j] = 127
    return y


def hysteresis(image, value):
    image_row, image_col = image.shape
    #print(image_row, image_col)
    top_to_bottom = image.copy()
 
    for row in range(2, image_row - 2):
        for col in range(2, image_col - 2):
            if top_to_bottom[row, col] == value:
                if top_to_bottom[row, col + 1] == 255 or top_to_bottom[row, col - 1] == 255 or top_to_bottom[row - 1, col] == 255 or top_to_bottom[
                row + 1, col] == 255 or top_to_bottom[
                row - 1, col - 1] == 255 or top_to_bottom[row + 1, col - 1] == 255 or top_to_bottom[row - 1, col + 1] == 255 or top_to_bottom[
                row + 1, col + 1] == 255:
                    top_to_bottom[row, col] = 255
                else:
                    top_to_bottom[row, col] = 0
                    
    bottom_to_top = image.copy()
 
    for row in range(image_row - 2, 2, -1):
        for col in range(image_col - 2, 2, -1):
            #print(row, col)
            if bottom_to_top[row, col] == value:
                if bottom_to_top[row, col + 1] == 255 or bottom_to_top[row, col - 1] == 255 or bottom_to_top[row - 1, col] == 255 or bottom_to_top[
                row + 1, col] == 255 or bottom_to_top[
                row - 1, col - 1] == 255 or bottom_to_top[row + 1, col - 1] == 255 or bottom_to_top[row - 1, col + 1] == 255 or bottom_to_top[
                row + 1, col + 1] == 255:
                    bottom_to_top[row, col] = 255
                else:
                    bottom_to_top[row, col] = 0
 
    right_to_left = image.copy()
 
    for row in range(2, image_row - 2):
        for col in range(image_col - 2, 2, -1):
            if right_to_left[row, col] == value:
                if right_to_left[row, col + 1] == 255 or right_to_left[row, col - 1] == 255 or right_to_left[row - 1, col] == 255 or right_to_left[
                row + 1, col] == 255 or right_to_left[
                row - 1, col - 1] == 255 or right_to_left[row + 1, col - 1] == 255 or right_to_left[row - 1, col + 1] == 255 or right_to_left[
                row + 1, col + 1] == 255:
                    right_to_left[row, col] = 255
                else:
                    right_to_left[row, col] = 0
 
    left_to_right = image.copy()
 
    for row in range(image_row - 2, 2, -1):
        for col in range(2, image_col - 2):
            if left_to_right[row, col] == value:
                if left_to_right[row, col + 1] == 255 or left_to_right[row, col - 1] == 255 or left_to_right[row - 1, col] == 255 or left_to_right[
                row + 1, col] == 255 or left_to_right[
                row - 1, col - 1] == 255 or left_to_right[row + 1, col - 1] == 255 or left_to_right[row - 1, col + 1] == 255 or left_to_right[
                row + 1, col + 1] == 255:
                    left_to_right[row, col] = 255
                else:
                    left_to_right[row, col] = 0

    final_image = top_to_bottom + bottom_to_top + right_to_left + left_to_right
 
    final_image[final_image > 255] = 255
 
    return final_image
