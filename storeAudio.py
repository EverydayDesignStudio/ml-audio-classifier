import csv
import os

def storeAudio(audiopath,categorypath = r'D:\mitacs\audio classification\audio_category'):
    classify_data = []
    print(audiopath)
    with open(audiopath + '\\slice_result.csv', "r") as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # 读取第一行每一列的标题
        for row in reader:
            classify_data.append(row)
        audiolength = str(classify_data[-1][0])
        audiotime = str(classify_data[-2][0])
        audiocategoty = classify_data[-3]
        for i in range(1,len(audiocategoty)):
            if i%2==1:
                with open(categorypath+'\\'+audiocategoty[i]+'.csv', 'a+', encoding='utf8', newline='') as outputfile:
                    writer = csv.writer(outputfile)
                    path=audiopath+'.wav'
                    possibility=audiocategoty[i+1]
                    output=[path,audiotime,audiolength,possibility]
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
    for i in range(2,len(directory)):
        storeAudio(directory[i])




