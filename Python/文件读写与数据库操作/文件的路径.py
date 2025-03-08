import os
"""
路径中/与\\效果一致
"""
# 相对路径: 文件名无盘符
# open('t.txt','r')
# 当前文件夹下
# open('../t.txt','r')
# 当前文件夹上一层文件夹下
# open('文件读写与数据库操作/t.txt','r')
open('\\X\\Python\\文件读写与数据库操作\\t.txt','a',encoding='utf-8')
# 当前盘符根文件夹下

# 绝对路径形式 包含盘符
print(os.getcwd()) #获取当前文件夹
os.chdir('T:/X') #改变当前文件夹到指定文件夹下
print(os.getcwd())