import datetime
#from IPython.display import Image
import time
from PIL import Image
import os
import pygame
from base_func import readcsv,showphoto,get_filelist
from drowFathers import drowFathers
pygame.mixer.init()
path=r'D:\mitacs\audio classification\FOLDER01'
audioname='STE-112'
audiodata = readcsv(r'D:\mitacs\audio classification\FOLDER01\audiotime2.csv')
photodata = readcsv(r'D:\mitacs\image\photo\phototime.csv')
phototime = []
classify_data = readcsv(path + '\\' + audioname + '\\' + 'slice_result.csv')
for audio in audiodata:
    if audio[0] == path+'\\'+audioname + '.wav':
        starttime = datetime.datetime.strptime(audio[3], '%Y-%m-%d %H:%M:%S')
        print(starttime)
        #files= os.listdir(os.)
        showphoto(starttime)
    slices =get_filelist(path + '\\' + audioname)
    for i in range(0,len(slices)):
        if os.path.splitext(slices[i])[-1][1:] == "wav":
            g=drowFathers(classify_data[i],name='test')
            Image("test.gv.png", width=500, height=500)
            track = pygame.mixer.music.load(path+"\\"+slices[i])
            print(path+"\\"+slices[i])
            pygame.mixer.music.play()
            print(classify_data[i])
            print(type(classify_data[i]))
            time.sleep(8)