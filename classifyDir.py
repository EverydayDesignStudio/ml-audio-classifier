import csv
import os
import classify10
import modifytime
import audiolength
def classifyDir(path):
    #path = (r"D:\mitacs\audio classification\FOLDER01\STE-000")
    with open('%s\\slice_result.csv'%path,'w',encoding='utf8',newline='') as outputfile:
        #outputfile.write(['time','label1','probability1','label2','probability2','label3','probability3','label4','probability','label5','probability5'])
        writer = csv.writer(outputfile)
        audiomodifytime=modifytime.modifytime(path+'.wav')
        length=audiolength.audiolength(path+'.wav')
        writer.writerow(['time','label1','probability1','label2','probability2','label3','probability3','label4','probability','label5','probability5'])
        dir_class={}
        files= os.listdir(path)
        for i in range(0, len(files)):
            if os.path.splitext(files[i])[-1][1:] == "wav":
                file_class=classify10.classify10(path+'\\'+files[i])
                #print(file_class)
                #writer.writerow(file_class)
                output=[str(8*(i))]
                for label in file_class:
                    #print(label)
                    output.append(label)
                    #print(file_class[label])
                    output.append(file_class[label])
                    if label in dir_class:
                        dir_class[label] = dir_class[label] + file_class[label] / (len(files)-1)
                    else:
                        dir_class[label] = file_class[label] / (len(files)-1)
                writer.writerow(output)
        dir_class = sorted(dir_class.items(),reverse=True,key=lambda x:x[1])
        audio_category=['whole']
        for label in dir_class:
            audio_category.append(label[0])
            audio_category.append(label[1])
        print(type(dir_class))
        print(audio_category)
        writer.writerow(audio_category)
        writer.writerow([audiomodifytime])
        writer.writerow([length])
        return dir_class

if __name__=='__main__':
    for i in range(110,138):
        path = (r"D:\mitacs\audio classification\FOLDER01\STE-%s"%i)
        if os.path.exists(path):
            dir_class=classifyDir(path)
            print(dir_class)
        #print(path)
