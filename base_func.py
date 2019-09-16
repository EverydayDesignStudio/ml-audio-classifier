import datetime
import csv
def readcsv(path):
    data = []
    with open(path,'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # 读取第一行每一列的标题
        for row in reader:
            data.append(row)
        return data

from PIL import Image
def showphoto(starttime,phototimefile = r'D:\mitacs\image\photo\phototime.csv'):
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
            return

import os
def get_filelist(file_path):
    dir_list = os.listdir(file_path)
    if not dir_list:
        return
    else:
        # 注意，这里使用lambda表达式，将文件按照最后修改时间顺序升序排列
        # os.path.getmtime() 函数是获取文件最后修改时间
        # os.path.getctime() 函数是获取文件最后创建时间
        dir_list = sorted(dir_list,  key=lambda x: os.path.getmtime(os.path.join(file_path, x)))
        # print(dir_list)
        return dir_list

import csv
def name2id(name):
    with open(r'D:\mitacs\audio classification\label.csv', "r") as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # 读取第一行每一列的标题
        for row in reader:
            if row[1]==name:
                return row[0]

def id2name(id):
    with open(r'D:\mitacs\audio classification\label.csv', "r") as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # 读取第一行每一列的标题
        for row in reader:
            if row[0]==id:
                return row[1]