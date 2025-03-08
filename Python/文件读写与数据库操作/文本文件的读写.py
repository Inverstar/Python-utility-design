# 文本文件读写
"""
    open打开文件, 返回值设为变量f
    f.write 写入
    f.readlines 读取全部文件内容
    f.readline 读取文件一行
    f.close() 函数关闭文件
    f.read() 返回字符串文件内容

"""
a = open('T:\\X\\Python\\文件读写与数据库操作\\t.txt','w',encoding='utf-8')
# 'w' 表示写入, 用此种方式打开文件. 文件若存在则会被覆盖
a.write("good\n")
a.write('好耶!\n')
a.close()


f = open('T:\\X\\Python\\文件读写与数据库操作\\t.txt','r',encoding='utf-8')
lines = f.readlines()
print(lines)

print(f) # 空列表?
f.close()
f = open('T:\\X\\Python\\文件读写与数据库操作\\t.txt','r',encoding='utf-8')
print(f) # 空列表?
for x in f:
    print(x,end='')
f.close()
for x in lines:
    print(x,end='')

f = open('T:\\X\\Python\\文件读写与数据库操作\\t.txt','a',encoding='utf-8')
f.write('我中了!\n')
f.write('畜生,你中了什么?\n')
f.close()