import csv
import os
import time, datetime
def storeSlice(audiopath,categorypath = r'D:\mitacs\audio classification\slice_category'):
    classify_data = []
    with open(audiopath + '\\slice_result.csv', "r") as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # 读取第一行每一列的标题
        for row in reader:
            classify_data.append(row)
        audiolength = float(classify_data[-1][0])
        audiotime = datetime.datetime.strptime(str(classify_data[-2][0]), "%Y.%m.%d %H:%M:%S")
        print(type(audiotime))
        audiocategoty = classify_data[-3]
        for slice in range(0,len(classify_data)-4):
            slice_data=classify_data[slice]
            for label in range(1,len(slice_data)):
                if label % 2 == 1:
                    with open(categorypath+'\\'+slice_data[label]+'.csv', 'a+', encoding='utf8', newline='') as outputfile:
                        writer = csv.writer(outputfile)
                        slicetime = audiotime + datetime.timedelta(seconds=8*int(classify_data[slice][0]))
                        slicename = 'slice%s.0SecsTo%d.0Secs.wav' % (slice_data[0], int(slice_data[0])+10)
                        path=audiopath+'\\'+slicename
                        possibility=slice_data[label+1]
                        classification = classify_data[slice]
                        output=[path,slicetime,possibility,classification]
                        writer.writerow(output)
        slice_data = classify_data[-4]
        for label in range(1,len(slice_data)):
            if label%2 == 1:
                with open(categorypath + '\\' + slice_data[label] + '.csv', 'a+', encoding='utf8',
                          newline='') as outputfile:
                    writer = csv.writer(outputfile)
                    #audiolength=round(audiolength,3)
                    slicename = 'slice%s.0SecsToEndFileAt%-6.3fSecs.wav' %(slice_data[0], audiolength)
                    print(slicename)
                    path = audiopath + '\\'+slicename
                    print(path)
                    possibility = slice_data[label + 1]
                    classification=classify_data[-4]
                    slicetime = audiotime + datetime.timedelta(seconds=8*int(classify_data[-4][0]))
                    output = [path, slicetime, possibility,classification]
                    writer.writerow(output)

if __name__ == '__main__':
    dirpath = r'D:\mitacs\audio classification\FOLDER01'
    files = os.listdir(dirpath)
    directory = []
    for file in files:
        filepath = os.path.join(dirpath,file)
        if os.path.isdir(filepath):
            directory.append(filepath)
    print(directory)
    for i in range(0,len(directory)):
        storeSlice(directory[i])




