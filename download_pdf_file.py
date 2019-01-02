# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 20:55:50 2019

@author: Jingdong
"""
import requests
fname ='Family_Album_USA.txt'

with open(fname) as f:
    for line in f:
        if 'http:' in line:
            url=line.strip()            
            response = requests.get(url)
            filename=url.split('/')[-1]
            with open(filename, 'wb') as f2:
                f2.write(response.content)
             


url='http://www.lovelylanguage.ru/download/family-album-usa/Episode-%206-hanksgiving-Family-Album-USA-Act-1.pdf'
response = requests.get(url)
filename=url.split('/')[-1]
with open(filename, 'wb') as f2:
    f2.write(response.content)
