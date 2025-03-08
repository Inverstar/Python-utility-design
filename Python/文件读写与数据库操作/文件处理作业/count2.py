import sys
f=open("finalscore.txt","r",encoding="utf-8")
score=f.readlines()
f.close()
#print(score)
a=open("id.txt","r",encoding="utf-8")
students=a.readlines()
a.close()
students.sort()
#print(students)
#新建字典dct，键为学号，值为做题数量
dct={}
for i in score:
    record=i.split("\t")
    if record[2].isdigit():
        chengJi=int(record[2])
    else:
        chengJi=int(record[3])
    dct[record[1]]=dct.get(record[1],0) + chengJi
#print(dct)
#查找和计算成绩
lst=[]
for j in students:
    ID,name=j.split("\t")
    count = 0      #count做题数量
    for k in dct.keys():  #遍历字典的键
        if ID in k or name in k:
            count=dct[k]
    if count==0:
        y=0
    elif count==1:
        y=50
    elif count==2:
        y=60
    else:
        y=60+4*(count-2)
    lst.append(ID+"\t"+name.strip()+"\t"+str(count)+"\t"+str(y)+"\n")
#print(lst)
f=open(sys.argv[1],"w",encoding="utf-8")
f.write("学号\t姓名\t题数\t分数\n")
for s in lst:
    f.write(s)
