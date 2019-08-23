# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 13:42:16 2019

@author: jli
"""

import os

def getFileSize(filePath, size=0):
    for root, dirs, files in os.walk(filePath):
        for f in files:
            size += os.path.getsize(os.path.join(root, f))
    return size
dataPath=r'C:\jliu'
for root, dirs, files in os.walk(dataPath):   
    if len(root.split(os.sep))<5: 
        size=getFileSize(root) /1024**3
         
        print ('size={:10.3} GB, path={}'.format(size, root))   
        


