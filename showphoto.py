from readcsv import readcsv
import datetime
from PIL import Image
def showphoto(path,starttime,phototimefile=r'D:\mitacs\image\photo\phototime.csv'):
    photodata = readcsv(phototimefile)
    phototime = []
    for i in range(0, len(photodata)):
        phototime.append(datetime.datetime.strptime(photodata[i][1], '%Y-%m-%d %H:%M:%S'))
        print(phototime[i])
        if phototime[i] > starttime:
            if (phototime[i] - starttime) > (starttime - phototime[i - 1]):
                img = Image.open(photodata[i - 1][0])
                print(photodata[i - 1][0])
            else:
                img = Image.open(photodata[i][0])
                print(photodata[i][0])
            img.show()

