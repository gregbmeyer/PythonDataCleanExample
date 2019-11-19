#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 21:29:03 2019

@author: greg
"""

import pandas as pd

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def setBinaryCat(inputString):
    tempStr = str(inputString)
    #print(" binary cat var=" + str(tempStr) + ';')
    if not tempStr == '1':
        tempStr = '0'
    else:
        tempStr = '1'
    return tempStr


candyDF = pd.read_csv("candyhierarchy2017.xlsx") 
candyDF = candyDF.replace('nan', 'unk')
print("read into memory data set candyhierarchy2017.xlsx")
print("candyDF shape =", candyDF.shape)
candyDF.dropna()
print('After dropping NA missing values:')
print("candyDF shape =", candyDF.shape)
#print first 10 rows
print(candyDF[:10])