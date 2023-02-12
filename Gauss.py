# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:36:04 2023

@author: asier
"""
import numpy as np

A=np.matrix([[2.0,3.0,4.0,5.0],[6.0,15.0,19.0,23.0],[8.0,42.0,60.0,70.0],[12.0,60.0,1.0,17.0]])
b=np.array([5.0,30.0,98.0,144.0])

def Gauss(A,b):

    n=np.linalg.matrix_rank(A)
    x=np.zeros(n)
    Ab=np.c_[A,b]
    for j in range(n-1):
        for i in range(j,n-1):
            a=Ab[i+1,j]
            m=a/(Ab[j,j])
            for k in range(n+1):
                Ab[i+1,k]=Ab[i+1,k]-Ab[j,k]*m
    
    for r in range(n-1,-1,-1):
        m=0
        for i in range(r+1,n):
            m=m+Ab[r,i]*x[i]
        x[r]=(Ab[r,n]-m)/(Ab[r,r])

    print(Ab)
    print(x)
            
print(A)
print(b)
Gauss(A,b)