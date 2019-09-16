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
if __name__=='__main__':
    print(name2id('Vehicle'))
    print(id2name('/m/07yv9'))