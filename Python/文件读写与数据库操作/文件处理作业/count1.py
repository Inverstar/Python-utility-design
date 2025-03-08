#coding=utf-8
import re
import sys
#使用Readfile函数，为了简化代码量，都是读取文件
#该函数对于本题的作用，把finalscore用readlines读到一个字符串列表score里面，列表的每个元素都是一行，
# 把id.txt全部读到一个列表里面，每个元素一行，就是一个学生的信息。

def Readfile(finafile,file):
    try:
        f1 = open(finafile,'r',encoding='utf-8')
        f2 = open(file,'r', encoding='utf-8')
    except Exception as e:
        print(e)
        return 0
    score = f1.readlines()
    students=f2.readlines()
    f1.close()
    f2.close()
    #把这个列表排序，就得到了按学号排序的学生列表 students
    students.sort()
    #对 students 里的每个元素，split出学号部分和姓名部分
    for l in students:
        line=l.split()
        #然后到整个 score里面去找，学号部分或姓名部分如果能够在score里面找到，
        # split找到的那个score元素，得到分数，再算成绩，输出。
        if Search(line[0], score) != -1 or Search(line[1], score) != -1:
            i = Search(line[0], score)
            if i == -1:
                i = Search(line[1], score)
            l1 = re.split('\t', score[i])
            a = int(l1[3])
            agrade = CountGrade(a)
            fout.write("%s\t%s\t%d\t%d\n" % (line[0], line[1], a, agrade))
        else:
            fout.write("%s\t%s\t%d\t%d\n" % (line[0], line[1], 0, 0))

#定义查找函数Search
def Search(a,b):
    for i in range(len(b)):
        if a in b[i]:
            return i
    return -1

#统计分数函数Countgrade
def CountGrade(grade):
    if grade==1:
        x=50
    elif grade==2:
        x=60
    elif grade>2:
        x=60+4*(grade-2)
    else:
        x=0
    return x

if __name__ == "__main__":
    fout = open(sys.argv[1], 'w', encoding='utf-8')
    fout.write("学号\t姓名\t题数\t分数\n")
    Readfile('finalscore.txt','id.txt')
    fout.close()
