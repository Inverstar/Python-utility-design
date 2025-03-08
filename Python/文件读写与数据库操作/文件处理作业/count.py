import sys
for x in enumerate(sys.argv):
    print(x)
print(sys.argv)
# sys.argv 是字符串列表
try:
    infile = open("T:\\X\\Python\\文件读写与数据库操作\\文件处理作业\\finalscore.txt",'r',encoding='utf-8')
    while True:
        datal = infile.readline()
        if datal == "":
            break
        datal = datal.strip()
        print(datal)
    infile.close()
except Exception as e:
    print(e)