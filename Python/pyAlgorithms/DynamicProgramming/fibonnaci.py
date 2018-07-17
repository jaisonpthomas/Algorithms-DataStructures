# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 18:08:10 2018

@author: Jaison Thomas
"""

def fibEfficientArray(n):
    fibArr = [0]*(n+1)
    fibArr[0] = 1
    fibArr[1] = 1
    for i in range(2, n+1):
        fibArr[i] = fibArr[i-1] + fibArr[i-2]
    return fibArr[n]

def fibEfficientDict(n):
    fibDict = {0:1, 1:1}
    for i in range(2, n+1):
        fibDict[i] = fibDict[i-1] + fibDict[i-2]
    return fibDict[n]

fibArrayAnswer = fibEfficientArray(1000000)
fibDictAnswer = fibEfficientDict(1000000)