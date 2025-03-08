import os
print(os.getcwd()) # 求程序的当前文件夹
os.chdir('T:/X') # 将当前文件夹设为选定文件夹
print(os.getcwd())
print(os.listdir(os.getcwd()))
# 返回一个列表, 包含文件夹下的子文件夹名和文件名
# os.mkdir('SQL')
# 创建一个文件夹
print(os.listdir(os.getcwd()))

os.chdir('T:/X/Python')
print(os.getcwd())
print(os.path.isfile('文件读写与数据库操作/t.txt'))
a = os.path.getsize('文件读写与数据库操作/t.txt')
print(a) # a 单位为字节
os.remove('文件读写与数据库操作/t.txt')
# 删除文件
# os.rmdir('SQL')
# 删除空文件夹SQL, 非空删除失败
# os.rename(x,y) 将文件夹或文件x改为name, 若包含地址连位置也会变化, 前提是被修改文件或文件夹存在
# shutil.copyfile(x,y) 拷贝文件x到y, 若y本来存在则会覆盖