import csv
import os
import datetime
from modifytime import modifytime
from audiolength import audiolength
path=r'D:\mitacs\audio classification\FOLDER01'
with open(path+'\\audiotime2.csv','w',encoding='utf8',newline='') as outputfile:
    writer = csv.writer(outputfile)
    writer.writerow(['path', 'modifytime','length','starttime'])
    files = os.listdir(path)
    for i in range(0, len(files)):
        if os.path.splitext(files[i])[-1][1:] == "wav":
            # print(type(file_class))
            file_path = path + '\\' + files[i]
            file_modifytime = modifytime(file_path)
            file_modifytime = datetime.datetime.strptime(file_modifytime, '%Y-%m-%d %H:%M:%S')
            audio_length=audiolength(file_path)
            if file_modifytime < datetime.datetime.strptime( '2018-08-01 11:08:36', '%Y-%m-%d %H:%M:%S'):
                file_modifytime=file_modifytime+ datetime.timedelta(days = 4224, hours=21)
            file_starttime = file_modifytime - datetime.timedelta(seconds=audio_length)
            writer.writerow([file_path,file_modifytime,audio_length,file_starttime])
