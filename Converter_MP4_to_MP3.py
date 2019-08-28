# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 20:55:50 2019
clip = mp.VideoFileClip(filemp4).subclip(0,20) # converter first 20 seconds
clip = mp.VideoFileClip(filemp4) # converter all mp4 file to mp3 file
clip.audio.write_audiofile(filemp3)           
@author: Jingdong
"""


import moviepy.editor as mp
import os


directory=r'E:\****'
os.chdir(directory)
mp4_file_list=[]
for root, dirs, files in os.walk(directory):
   for f in files:
       filename = os.path.join(root, f)
       if filename.endswith('.mp4'):
           mp4_file_list.append(filename)

#clip = mp.VideoFileClip(filemp4).subclip(0,20) # converter first 20 seconds

#clip.audio.write_audiofile(filemp3)           
           
for filemp4 in  mp4_file_list:
    #filemp3=filemp4.split('.')[0]+'.mp3' 
    filemp3=filemp4.replace('.mp4','.mp3')
    if not os.path.isfile(mp3_filename):
         with mp.VideoFileClip(filemp4) as clip:    
            clip.audio.write_audiofile(filemp3)


 ###########################################################################################        

dataPath=r'E:\**'

MP4_file_list=[]
for root, dirs, files in os.walk(dataPath):
    for fname in files:            #if '5001' in fname and fname.endswith('.xlsx') and not fname.startswith('~'):
        if fname.endswith('.mp4') and not fname.startswith('~'):
            #print(root,dirs,fname)
            filename=os.path.join(root, fname)                             
            MP4_file_list.append(filename) 
for i in range(len(MP4_file_list)):
    mp4_filename=MP4_file_list[i]
    mp3_filename=mp4_filename.replace('.mp4','.mp3')
    if not os.path.isfile(mp3_filename):
        try:
            clip = mp.VideoFileClip(mp4_filename)
            clip.audio.write_audiofile(mp3_filename)
            clip.close()
        except:
            print ('Could convert {}'.format(mp4_filename))
        
