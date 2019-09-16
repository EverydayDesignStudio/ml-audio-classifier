import csv
def readcsv(path):
    data = []
    with open(path,'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # 读取第一行每一列的标题
        for row in reader:
            data.append(row)
        return data