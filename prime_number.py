# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 21:43:27 2018

@author: Jingdong
"""

import math,time
import numpy as np
import pandas as pd

def prime(N):
    P=[2]
    for i in range(3,N,2):
        max = int(i**0.5)  
        isprime=True        
        for j in P:
            if i%j==0 :
               isprime=False
               break
            if j > max:
               break  
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
               break  # it is very important
        if isprime:
            P.append(i)
    return P           


def prime3(N):
    P=[2]
    
    for i in range(3,N,2):        
        isprime=True        
        for j in range(3,int(math.sqrt(i))+1,2):
            if i%j==0:
               isprime=False
        if isprime:
            P.append(i)
    return P           

def prime4(N):
    P=np.array(2)      
    for i in range(3,N,2):                  
        K=P[P<=math.sqrt(i)] 
        isprime=True         
        for j in K:             
            if i%j==0:                
                isprime=False                
                break         
        if isprime:             
            P=np.append(P,i)
    return P           

def prime5(N):
    P=[2]
    for i in range(3,N,2):
        K= [k for k in P if k<=math.sqrt(i)]
        isprime=True        
        for j in K:
            if i%j==0:
               isprime=False
               break
        if isprime:
            P.append(i)
    return P           


def calPrime(n):
    primes = []

    for i in range(3, n + 1, 2):
        max = int(i ** .5)
        for prime in primes:
            if prime > max:
                primes.append(i)
                break
            elif not i % prime:
                break
        else:
            primes.append(i)

    if n >= 2:
        primes.insert(0, 2)

    return primes


result=pd.DataFrame(columns=['N','t1','t2','t3','t4','t5','len(P)'])

import pickle
if 1:
    newfile='prime_number2.txt'
    with open(newfile,"rb") as f2:
        result = pickle.load(f2)
    k0=len(result)
else:
    k0=1

for k in range(k0,10):
    N=10**k
    D=pd.DataFrame(columns=['N','t1','t2','t3','t4','t5','len(P)'])
    
    start = time.time()
    P=prime(N)
    end = time.time()
    D.loc[0,'N']=N
    D.loc[0,'t1']=round(end-start,5)
    
    D.loc[0,'len(P)']=len(P)
   
    
    
    start = time.time()
    P=prime2(N)
    end = time.time()
    D.loc[0,'t2']=round(end-start,5)
    if D.loc[0,'len(P)']!=len(P):
        print('len(P) is not equal in prime2')
  
    
    start = time.time()
    P=prime3(N)
    end = time.time()
    D.loc[0,'t3']=round(end-start,5)
    if D.loc[0,'len(P)']!=len(P):
        print('len(P) is not equal in prime3')

    start = time.time()
    P=prime4(N)
    end = time.time()
    D.loc[0,'t4']=round(end-start,5)
    if D.loc[0,'len(P)']!=len(P):
        print('len(P) is not equal in prime4')
    
    if k<7:
        start = time.time()
        P=prime5(N)
        end = time.time()
        D.loc[0,'t5']=round(end-start,5)    
        if D.loc[0,'len(P)']!=len(P):
            print('len(P) is not equal in prime2')
    else:
        D.loc[0,'t5']= float('inf')  
        """
        D.loc[0,'t5']= float('nan')  
        """
        
        

 
    print(D)
    result=result.append(D)
    
    
    result=result.reset_index()
    if 'index' in result.columns:
        result.drop(['index'],axis=1,inplace=True)
    if 'level_0' in result.columns:
        result.drop(['level_0'],axis=1,inplace=True)
    
    savefile='prime_number2.txt'
    with open(savefile,"wb") as f1:           
        pickle.dump(result, f1)


    # N=100000, 3328.530927181244， len(P)= 78498
