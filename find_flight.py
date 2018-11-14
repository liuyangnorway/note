# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 12:08:03 2018

@author: Jingdong
"""

import requests
from bs4 import BeautifulSoup
import json
import jsonpath
import datetime
import pandas as pd
import copy
import time
def getHTMLText(url):
    try:
        r=requests.get(url,timeout=300)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r
    except:
        print("产生异常")
        return "产生异常"
#
Origin='OSL.METROPOLITAN_AREA'
Destination='LPA.AIRPORT'
d0=datetime.date(2018,12,22)
delta = datetime.timedelta(days=1)
df=pd.DataFrame(columns=['Origin','Destination','DepartureDate','ReturnDate','case','durations','price'])
for i in range(0,6):
    d1=d0+ delta*i
    DepartureDate=d1.strftime("%d.%m.%Y")
    url=[]
    json_url=[]
    for j in range(5,9):
        d2 = d1 + delta*j
        ReturnDate=d2.strftime("%d.%m.%Y")            
        url='https://www.finn.no/reise/flybilletter/resultat?tripType=roundtrip&requestedOrigin={}&requestedDestination={}&requestedDepartureDate={}&requestedReturnDate={}&numberOfAdults=2&childAges=6&childAges=10&childAges=13&cabinType=economy'\
        .format(Origin,Destination,DepartureDate,ReturnDate)
        
        html = getHTMLText(url)
        for i in range(0,5):            
            if  isinstance(html,str):
                time.sleep(5) 
                html = getHTMLText(url)         
        if  isinstance(html,str):        
            print('Could not get data from url={}'.format(url))  
            continue
        
        soup = BeautifulSoup(html.text, 'lxml')
        tag = soup.find_all('input',attrs={'id':'resultUrl'})
        id=tag[0]['value']
        json_url='https://www.finn.no/reise/flybilletter/{}'.format(id)
        time.sleep(5)
        print('{}  |  {} | {}'.format(DepartureDate,ReturnDate,json_url))
        html2 = getHTMLText(json_url)                
        for i in range(0,5):            
            if  isinstance(html2,str):
                time.sleep(5) 
                html2 = getHTMLText(url)         
        if  isinstance(html2,str):        
            print('Could not get data from url={}'.format(json_url))  
            continue
        
        json_data = json.loads(html2.text)
        bestOffers=json_data['bestOffers']
        Best=copy.deepcopy(bestOffers['AGONY'])
        Best_price=copy.deepcopy(bestOffers['PRICE'])
        Best_time=copy.deepcopy(bestOffers['DURATION'])
        Best['durations'][0]='{}t{}'.format(Best['durations'][0]//60,Best['durations'][0]%60)
        Best['durations'][1]='{}t{}'.format(Best['durations'][1]//60,Best['durations'][1]%60)
        Best_price['durations'][0]='{}t{}'.format(Best_price['durations'][0]//60,Best_price['durations'][0]%60)
        Best_price['durations'][1]='{}t{}'.format(Best_price['durations'][1]//60,Best_price['durations'][1]%60)
        Best_time['durations'][0]='{}t{}'.format(Best_time['durations'][0]//60,Best_time['durations'][0]%60)
        Best_time['durations'][1]='{}t{}'.format(Best_time['durations'][1]//60,Best_time['durations'][1]%60)
        
        
        
        df0= pd.DataFrame(columns=df.columns)
        df0.loc[0]=None
        df0.loc[0,'Origin']=Origin.split('.')[0]
        df0.loc[0,'Destination']=Destination.split('.')[0]
        df0.loc[0,'DepartureDate']= DepartureDate
        df0.loc[0,'ReturnDate']= ReturnDate
        df0.loc[0,'case']= 'Best'
        df0.loc[0,'durations']= Best['durations']
        df0.loc[0,'price']= Best['price']
        df0.loc[1]=df0.loc[0]
        df0.loc[2]=df0.loc[0]
        df0.loc[1,'durations']= Best_price['durations']
        df0.loc[1,'price']= Best_price['price']
        df0.loc[2,'durations']= Best_time['durations']
        df0.loc[2,'price']= Best_time['price'] 
        df0.loc[1,'case']= 'Best_price'      
        df0.loc[2,'case']= 'Best_time'           
        
        df = pd.concat([df,df0],ignore_index=True)
df.reset_index(drop=True,inplace=True)   
df.sort_values(by=['case','price'])
df1=df[df['case']=='Best']  
df1.sort_values(by=['case','price'])        

        

## price_list=jsonpath.jsonpath(json_data,"$..price")


    
    
    

