# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 21:43:27 2018

@author: Jingdong
"""

import math
def prime(N):
    P=[2]
    for i in range(3,N,2):
        K= [k for k in P if k<=math.sqrt(i)]
        isprime=True        
        for j in K:
            if i%j==0:
               isprime=False
        if isprime:
            P.append(i)
    return P           




def prime2(N):
    P=[2]
    for i in range(3,N,2):
        
        isprime=True        
        for j in range(3,int(math.sqrt(i))+1,2):
            if i%j==0:
               isprime=False
        if isprime:
            P.append(i)
    return P           

import time
start = time.time()
P=prime(10000)
end = time.time()
print(end-start)

start = time.time()
P2=prime2(10000)
end = time.time()
print(end-start)
