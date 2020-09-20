#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 18:22:15 2020

@author: raja
"""

import numpy as np

test_cases = np.array([[0.5,0.6,0.6,0.5],[0.5,0.7,0.7,0.4],[0.5,0.7,0.7,0.4],[0.5,0.7,0.7,0.4]])

def getContourCase(top,left,thres,cells):

    row = len(cells)
    col = len(cells[0])

    a = 0
    if (cells[left, top] > thres): #msb
        a = 1 #msb
    
    if (top+1 < col and cells[left, top+1] > thres):
        a = (a << 1) ^ 1
    else:
        a = (a << 1) ^ 0

    if (top+1 < col and left+1 < row and cells[left+1, top+1] > thres):
        a = (a << 1) ^ 1
    else:
        a = (a << 1) ^ 0
        
    if (left+1 < col and cells[left+1, top] > thres): #lsb
        a = (a << 1) ^ 1
    else:
        a = (a << 1) ^ 0
    
#    print(bin(a))        
    return a

def disambiguateSaddle(top,left,thres,cells):
    if ((cells[left, top] + cells[left+1, top+1] + cells[left, top+1] + cells[left+1, top])/4 >= thres):
        return True
    else:
        return False
    
def interpolate(v1,v2,t):
    return abs((t-v1)/(v2-v1))
    
def getCellSegments(top,left,thres,cells):
    results = 0
    return results
    

print(getContourCase(0,2,0.4,test_cases))
print(getContourCase(3,3,0.4,test_cases))

print(disambiguateSaddle(0,1,0.7,test_cases))
print(disambiguateSaddle(1,2,0.5,test_cases))

print(interpolate(2.5,1.5,1.2))
print(interpolate(2.5,1.5,2.5))

test_cases_1 = np.array([[0.5,0.6,0.6,0.5],[0.5,0.7,0.7,0.4],[0.5,0.7,0.7,0.4],[0.5,0.7,0.7,0.4]])
assert getCellSegments(3,3,0.9,test_cases_1) == []
test_cases_2 = np.array([[0.07339991, 0.38311005, 0.38311005, 0.07339991],[0.38311005, 0.99744795, 0.99744795, 0.38311005],[0.38311005, 0.99744795, 0.99744795, 0.38311005],[0.07339991, 0.38311005, 0.38311005, 0.07339991]])
result = getCellSegments(0,0,0.2,test_cases_2)
result[0].sort()
assert result == [[(0, 0.40876959985875827), (0.40876959985875827, 0)]]
test_cases_3 = np.array([[0.05,0.4,0.4,0.05],[0.4,0.9,0.9,0.4],[0.4,0.9,0.9,0.4],[0.05,0.4,0.4,0.05]])
result = getCellSegments(2,2,0.2,test_cases_3)
result[0].sort()
assert result == [[(2.571428571428571, 3), (3, 2.571428571428571)]]