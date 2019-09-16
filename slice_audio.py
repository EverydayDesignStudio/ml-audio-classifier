import os
import glob
from pydub import AudioSegment
import argparse
import audioread
import time
import re

#Function to slice up the audio.
def slice_audio(path, channels=1, outformat='wav', width=2, rate=44100, slice_length=10000, slide=8000):
    outformat = outformat.replace('.','').lower()
    #Allow the user to see their x-bit selection with this dictionary.
    width_translator = {1:'8-bit', 2:'16-bit', 4:'32-bit'}
    #For every file in the input list do processing.
    if os.path.isdir(path):
        files = [f for f in os.listdir(path) if re.match(r'(.*?)\.wav', f)]
        for i in range(0, len(files)):
            files[i] = path + '\\'+ files[i]
    #print(files)
    for file in files:
        fileName, fileExtension = os.path.splitext(file)
        print(fileName)
        print(fileExtension)
        #Print to screen the processing parameters.
        #os.makedirs('%s'%fileName)
        mkdir('%s'%fileName)
        with audioread.audio_open(file) as f:
            print ('\nConverting '+fileName+' from:')
            print (fileExtension+' to .'+outformat+';')
            print (str(f.channels)+' channel(s) to '+str(channels)+' channel(s);')
            print (str(f.samplerate)+' Hz to '+str(rate)+' Hz;')
            print ('Slicing '+str(f.duration*1000)+' ms file into '+str(slice_length)+' ms slices with a window slide of '+str(slide)+' ms;')
        #Store the file in RAM.
        sound = AudioSegment.from_file(file, fileExtension.replace('.','').lower())
        #Print the 'x-bit' conversion parameters.
        print (width_translator[sound.sample_width]+' to '+width_translator[int(width)]+'.\n')
        #Implement the user-selected or default (if nothing selected) parameters for processing.
        sound = sound.set_frame_rate(int(rate))
        sound = sound.set_sample_width(int(width))
        sound = sound.set_channels(int(channels))
        length_sound_ms = len(sound)
        length_slice_ms = int(slice_length)
        slice_start = 0
        #create audiosegment object
        #Begin slicing at the start of the file.
        while slice_start + length_slice_ms < length_sound_ms:
            sound_slice = sound[slice_start:slice_start+length_slice_ms]
            sound_slice.export(fileName+'/'+'slice'+str(slice_start/1000)+'SecsTo'+str((slice_start+length_slice_ms)/1000)+'Secs.'+outformat, format=outformat)
            slice_start += int(slide)
        #When the slice is abutting the end of the file, output that slice too.'
        if slice_start + length_slice_ms >= length_sound_ms:
            sound_slice = sound[slice_start:length_sound_ms]
            sound_slice.export(fileName+'/'+'slice'+str(slice_start/1000)+'SecsToEndFileAt'+str((length_sound_ms)/1000)+'Secs.'+outformat, format=outformat)


def mkdir(path):
    # 引入模块
    import os

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print(path + 'success')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' the directory has existed')
        return False