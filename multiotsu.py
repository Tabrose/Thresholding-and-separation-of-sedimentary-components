# -*- coding: utf-8 -*-
"""
Created on Wed May 11 20:02:06 2022

@author: Tabrose HOSSAIN
"""

import numpy as np
import otsu


def histogram_binning(hist, M=32, L=256):
    norm_hist = np.zeros((M, 1))
    N = L // M
    counters = [range(x, x+N) for x in range(0, L, N)]
    for i, C in enumerate(counters):
        norm_hist[i] = 0
        for j in C:
            norm_hist[i] += hist[j]
    norm_hist = (norm_hist / norm_hist.max()) * 100
    return norm_hist


def find_valleys(H):
    hsize = H.shape[0]
    probs = np.zeros((hsize, 1), dtype=int)
    costs = np.zeros((hsize, 1))
    for i in range(1, hsize-1):
        if H[i] > H[i-1] or H[i] > H[i+1]:
            probs[i] = 0
        elif H[i] < H[i-1] and H[i] == H[i+1]:
            probs[i] = 1
            costs[i] = H[i-1] - H[i]
        elif H[i] == H[i-1] and H[i] < H[i+1]:
            probs[i] = 3
            costs[i] = H[i+1] - H[i]
        elif H[i] < H[i-1] and H[i] < H[i+1]:
            probs[i] = 4
            costs[i] = (H[i-1] + H[i+1]) - 2*H[i]
        elif H[i] == H[i-1] and H[i] == H[i+1]:
            probs[i] = probs[i-1]
            costs[i] = probs[i-1]
    for i in range(1, hsize-1):
        if probs[i] != 0:
            probs[i] = (probs[i-1] + probs[i] + probs[i+1]) // 4
    valleys = [i for i, x in enumerate(probs) if x > 0]
    return valleys


def valley_estimation(hist, M=32, L=256):
    norm_hist = histogram_binning(hist, M, L)
    valleys = find_valleys(norm_hist)
    return valleys


def otsu_threshold_value(hist):
    opt, maximum = otsu.otsu_threshold(hist)
    return opt


def threshold_valley_regions(hist, valleys, N):
    thresholds = []
    for valley in valleys:
        start = (valley * N) - N
        end = (valley + 2) * N
        h = hist[start:end]
        sub_threshold, val = otsu.otsu_threshold(h)
        thresholds.append((start + sub_threshold, val))
    thresholds.sort(key=lambda x: x[1], reverse=True)
    try:
        thresholds, values = [list(t) for t in zip(*thresholds)]
    except:
        pass
    return thresholds



def Multithreshold_Otsu(hist, M=32, L=256):
    N = L // M
    valleys = valley_estimation(hist, M, L)
    thresholds = threshold_valley_regions(hist, valleys, N)
    return thresholds
