# 同样是使用递归的方式来处理文件夹里面的内容
import os

def getTotalSize(path):
    total = 0
    lst = os.listdir(path)
    for x in lst:
        FileName = path + '/' + x
        if os.path.isfile(FileName):
            FS = os.path.getsize(FileName)
            print(FileName,FS)
            total += FS
            # 直接得到文件夹大小
        else:
            total += getTotalSize(FileName)
            # 对文件夹进行递归
    return total
os.chdir('T:/X')
S = os.getcwd()
print(S)
print(int(getTotalSize(S)/1024),'KB')
