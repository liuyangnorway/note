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
    filemp3=filemp4.split('.')[0]+'.mp3' 
    with mp.VideoFileClip(filemp4) as clip:    
        clip.audio.write_audiofile(filemp3)
