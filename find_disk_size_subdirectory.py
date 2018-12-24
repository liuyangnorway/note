# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 17:22:40 2018

@author: Jingdong
"""
import os,time
import pandas as pd


path=r'E:\github'
path = os.path.normpath(path)
path.split(os.sep)
A=list(os.walk(path, topdown=False))

def find_subpath(path):
    import os
    for root, dirs, files in os.walk(path, topdown=False):  
        if root ==path:
            return root, dirs, files

def findfile(root, keywords):
    for fileDir, dirs, files in os.walk(root):
        for file in files:
            if keywords in file:
                full_path = os.path.join(fileDir, file)
                print(os.path.normpath(os.path.abspath(full_path)))
 
def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    if total_size<1024:
        size='{} Byte'.format(total_size)
    elif total_size<1024**2:
        size='{:0.2f} KB'.format(total_size/1024)
    elif total_size<1024**3:        
        size='{:0.2f} MB'.format(total_size/1024/1024)
    else:        
         size='{:0.2f} GB'.format(total_size/1024/1024/1024)
    
    return size,total_size
def size_in_MB_GB(total_size):
    if total_size<1024:
        size='{} Byte'.format(total_size)
    elif total_size<1024**2:
        size='{:0.2f} KB'.format(total_size/1024)
    elif total_size<1024**3:        
        size='{:0.2f} MB'.format(total_size/1024/1024)
    else:        
         size='{:0.2f} GB'.format(total_size/1024/1024/1024)
    
    return size
    


def find_size_subdir(directory='.'):
    #directory='E:\\'
    if directory=='.':
        directory = os.getcwd()
    df = pd.DataFrame(columns=['path','size','total_size'])
    root,dirs, files=find_subpath(directory)
    if 'Users' in dirs and root=='C:\\':
        print('remove folder: Users')
        dirs.remove('Users')
    for name in dirs:         
        path=os.path.join(root, name)
        size,total_size=get_size(path)
        
        df=df.append([{'path':path,'size':size,'total_size':total_size}])
      
    total_size = df['total_size'].sum()
    size = size_in_MB_GB(total_size)
    df=df.append([{'path':root,'size':size,'total_size':total_size}])
    df.reset_index(inplace=True)
    df.drop('index',axis=1,inplace=True)
    return df

directory='C:\\'
df=find_size_subdir(directory)
df.drop(len(df)-1,inplace=True)
directory='C:\\Windows'
df2=find_size_subdir(directory)
df=df.append(df2.iloc[-1])
total_size = df['total_size'].sum()
size = size_in_MB_GB(total_size)
df=df.append([{'path':directory,'size':size,'total_size':total_size}])
df.reset_index(inplace=True)
df.drop('index',axis=1,inplace=True)

savefile='{}_subfolder_size_{}.xlsx'.format('_'.join(directory.split(os.sep)).replace(':',''),time.strftime('%Y%m%d',time.localtime(time.time())))
df.to_excel(r'C:\tmp\{}'.format(savefile))

directory=r'C:\Users\Jingdong\AppData\Roaming'
df3=find_size_subdir(directory)

directory=r'C:\Users\Jingdong\AppData\Roaming\Apple Computer\MobileSync\Backup' ##very big files


directory=r'C:\Users\Jingdong'
df3=find_size_subdir(directory)




def test():           
    if not os.path.isdir(r'E:\test'):          
        os.mkdir(r'E:\test')
    
        os.mkdir(r'E:\test\A1')
        os.mkdir(r'E:\test\A2')
        os.mkdir(r'E:\test\A3')
        os.mkdir(r'E:\test\A4')
        os.mkdir(r'E:\test\A1\B11')
        os.mkdir(r'E:\test\A1\B12')
        os.mkdir(r'E:\test\A2\B21')
        os.mkdir(r'E:\test\A3\B31')
        os.mkdir(r'E:\test\A1\B11\C111')
    
    
    path=r'E:\test'
    os.chdir(r'E:\test')     
    ##length =len(path.split(os.sep))+1
    for root, dirs, files in os.walk(path, topdown=False):  
        if root ==path:
        ##if  len(root.split(os.sep))==length:
            print(dirs)
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))  

            
    for root, dirs, files in os.walk(path, topdown=False):
        print('root={}'.format(root))
        print('file:')
        for name in files:        
            print(os.path.join(root, name))
        
        print('Dirs: ')
        
        for name in dirs:
            print(os.path.join(root, name))  
        print('________________________ ')
    


 
    

