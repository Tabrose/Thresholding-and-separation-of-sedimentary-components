# -*- coding: utf-8 -*-
"""
Created on Wed May 11 20:02:06 2022

@author: Tabrose HOSSAIN
"""

import math
import numpy as np


def calcul_hist(img):
   row, col = img.shape
   y = np.zeros(256)
   for i in range(row):
      for j in range(col):
         y[img[i,j]] += 1
   return y


def count_pixel(h):
    count = 0
    for i in range(len(h)):
        if h[i]>0:
            count += h[i]
    return count


def weight(a, b, h):
    w = 0
    for i in range(a, b):
        w += h[i]
    return w


def mean(a, b, h):
    m = 0
    w = weight(a, b, h)
    for i in range(a, b):
        m += h[i] * i
    if m != 0.0:
        m /= float(w)
    else:
        m = 0
    return m


def variance(a, b, h):
    v = 0
    m = mean(a, b)
    w = weight(a, b)
    for i in range(a, b):
        v += ((i - m) **2) * h[i]
    v /= w
    return v


def otsu_threshold(h):
    cnt = count_pixel(h)
    threshold_values = {}
    for i in range(1, len(h)):
        wb = weight(0, i, h) / float(cnt)
        mb = mean(0, i, h)
        
        wf = weight(i, len(h), h) / float(cnt)
        mf = mean(i, len(h), h)
        
        V2b = wb * wf * (mb - mf)**2

        if not math.isnan(V2b):
            threshold_values[i] = V2b
        
    maximum = max(threshold_values.values())
    optimal_value = [k for k, v in threshold_values.items() if v == maximum]
    return optimal_value[0], maximum
