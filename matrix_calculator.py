# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 20:57:21 2023

@author: Admin
"""

def matrix_mult(x,y):
    
    assert len(x[0]) == len(y)
    
    result = [[0 for j in range(len(y[0]))] for i in range(len(x))]
    
    for i in range(len(x)): #iterating row-wise (first matrix)
        for j in range(len(y[0])): #iterating column-wise (second matrix)
            element = 0
            for k in range(len(x[0])): # along row of first matrix and column of second matrix:
                element += x[i][k] * y[k][j]
            result[i][j] = element
    return result

def matrix_addition(x, y):
    assert len(x[0]) == len(y[0]) and len(x) == len(y)
    result = [[0 for j in range(len(y[0]))] for i in range(len(x))]
    for i in range (len(x)):
        for j in range(len(y)):
            result[i][j] = x[i][j] + y[i][j]
    return result