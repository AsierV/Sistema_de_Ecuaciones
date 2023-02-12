# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 15:12:54 2023

@author: asier
"""

import numpy as np

A=np.matrix([[1.0,1.0,-1.0,0.0],[1.0,-1.0,0.0,1.0],[-1.0,0.0,1.0,1.0],[0.0,1.0,1.0,-1.0]])
b=np.array([1.0,1.0,1.0,1.0])

def Gauss(A,b):
    
    n=np.linalg.matrix_rank(A)
    x=np.zeros(n)
    Ab=np.c_[A,b]
    for j in range(n-1):
        for i in range(j,n-1):
            a=Ab[i+1,j]
            
            #******************************
            
            if(Ab[j,j]==0):
                f=0
                for t in range(n-1):
                    if(abs(Ab[j,t])>f):
                        f=abs(Ab[j,t])
                for o in range(n-1):
                    if(abs(Ab[o,j])==f):
                        break
                
                for i in range(n-1):
                    d=Ab[j,i]
                    c=Ab[o,i]
                    
                    Ab[o,i]=d
                    Ab[j,i]=c
            #******************************
            
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