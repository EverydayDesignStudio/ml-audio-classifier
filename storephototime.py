#get the modify time of each photo
import csv
import os
import datetime
from modifytime import modifytime
from google.cloud import vision
import io
path=r'D:\mitacs\image\photo'
def detect_labels(path):
    """Detects labels in the file."""
    client = vision.ImageAnnotatorClient()
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)
    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')
    return response
with open(path+'\\phototime.csv','w',encoding='utf8',newline='') as outputfile:
    writer = csv.writer(outputfile)
    writer.writerow(['path', 'time','labels'])
    files = os.listdir(path)
    for i in range(0, len(files)):
        if os.path.splitext(files[i])[-1][1:] == "jpg":
            # print(type(file_class))
            file_path = path + '\\' + files[i]
            file_modifytime = modifytime(file_path)
            file_modifytime = datetime.datetime.strptime(file_modifytime, '%Y-%m-%d %H:%M:%S')
            file_labels = detect_labels(file_path)
            print(file_labels)
            writer.writerow([file_path,file_modifytime,file_labels])
