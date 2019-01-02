# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 20:55:50 2019

@author: Jingdong
"""
import requests,os
from bs4 import BeautifulSoup 

fname ='url_link_list.txt'

with open(fname) as f:
    for line in f:
        if 'http:' in line:
            url=line.strip()            
            response = requests.get(url)
            filename=url.split('/')[-1]
            with open(filename, 'wb') as f2:
                f2.write(response.content)
        

def getHTMLText(url):
    import requests
    try:
        r=requests.get(url,timeout=300)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r
    except:
        print("Could not connect to server")
        return "Could not connect to server"

os.chdir(r'E:\Python\book')
my_url = 'http://slav0nic.org.ua/static/books/python/'     

html = getHTMLText(my_url)  

if not isinstance(html,str): 
    soup = BeautifulSoup(html.text, 'lxml') 
    current_link = ''
    url_list=[]
    for link in soup.find_all('a'):        
        current_link = link.get('href')    
        if not (current_link.endswith('/') or current_link.startswith('?')):      
            url_list.append(current_link)
        
for url in url_list:                   
    response = requests.get(my_url+url)            
    filename=url.split('/')[-1]            
    with open(filename, 'wb') as f2:
        print('Downloading book: {}'.format(url))                
        f2.write(response.content)
  
        

