from name2id import id2name, name2id
from graphviz import Digraph
from readcsv import readcsv

def drowFather2child(label_data,child,g):
    for label in label_data:
        if label[1] == child:
            g.append(label[1])
            g.append(id2name(label[4]))
            if label[4]=='/m/':
                return g
            else:
                drowFather2child(label_data,id2name(label[4]),g)

def drowFathers(slicelabel):
    label_data = readcsv(r'D:\mitacs\audio classification\label.csv')
    branch = []
    for z in range(1,len(slicelabel),2):
        drowFather2child(label_data, slicelabel[z], branch)
    print(branch)
    x = 0
    while x < len(branch):
        y = x + 2
        while y < len(branch):
            if branch[x] == branch[y] and branch[x + 1] == branch[y + 1]:
                branch.pop(y + 1)
                branch.pop(y)
            y = y + 2
        x = x + 2
    print(branch)
    branch2=list(map(lambda x: x.replace(' ','\n'),branch))
    print(branch2)
    slicelabel=list(map(lambda x: x.replace(' ','\n'),slicelabel))
    g = Digraph('测试图片',format="png")
    for x in range(1,len(slicelabel),2):
        print(slicelabel[x])
        color=round(8*float(slicelabel[x+1]),3)
        print(color)
        g.node(slicelabel[x],color='0.000 %f %f'%(color,color),shape='circle',width='2',height='2',penwidth='%f'%color)
    for i in range(0, len(branch) - 1, 2):
        g.node(branch2[i],shape='circle',width='2',height='2')
        g.node(branch2[i + 1],shape='circle',width='2',height='2')
        g.edge(branch2[i + 1], branch2[i])
        # i = i+2
    #print(g.source)
    g.view()



if __name__=='__main__':
    slicelabel=['72', 'Music', '0.5053558349609375', 'Field recording', '0.10353360325098038', 'Musical instrument',
     '0.09679726511240005', 'Outside, rural or natural', '0.07840725779533386', 'Bird', '0.06056944280862808']
    drowFathers(slicelabel)