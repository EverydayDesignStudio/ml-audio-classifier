import json
import csv
def encodeLabel(ontology,ID,fatherID,code,i):
    with open(r'D:\mitacs\audio classification\label.csv', 'a+', encoding='utf8', newline='') as outputfile:
        writer = csv.writer(outputfile)
        for label in ontology:
            if label['id'] == ID:
                if not (fatherID == 'from child'):
                    if not (label.get('code')):
                        label['i'] = 0
                    code2 = list(code)
                    code2.append(i)
                    label['code'] = code2
                    print(label['code'])
                    label['fatherID'] = fatherID
                    output=[label['id'],label['name'],label['description'],label['child_ids'],label['fatherID'],label['code']]
                    writer.writerow(output)
                if label['i'] < len(label['child_ids']):
                    label['i']=label['i']+1
                    nextID=label['child_ids'][label['i']-1]
                    print('nextid is %s'%nextID)
                    thisID=label['id']
                    print('this ID is %s'%thisID)
                    thisCode=label['code']
                    print('this code is %s'%thisCode)
                    print(label['i'])
                    print('**********************************************************************************')
                    encodeLabel(ontology,nextID,thisID,thisCode,label['i'])
                else:
                    print('##################################################################################')
                    print('fatherID is %s'%fatherID)
                    encodeLabel(ontology,label['fatherID'],'from child','','')

if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(100000)  # 例如这里设置为十万
    with open(r'D:\mitacs\audio classification\label.csv', 'w', encoding='utf8', newline='') as outputfile:
        writer = csv.writer(outputfile)
        writer.writerow(['ID', 'name', 'description', 'child_ids', 'father_id','code'])
    f = open(r'D:\mitacs\audio classification\ontology-master\ontology.json',encoding='utf-8')
    res = f.read()
    ontology = json.loads(res)
    encodeLabel(ontology, "/m/", '', [], 0)