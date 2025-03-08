# 由于rmdir()只能删除空文件夹, 所以需要使用递归的方式来删除其下的文件再删文件夹
"""
 !!!警告!!! 
 使用此函数删除的文件夹无法恢复,慎用$
"""
import os
def powerRmDir(path):
    lst = os.listdir(path)
    for x in lst:
        FileName = path + '/' + x
        if os.path.isfile(FileName):
            os.remove(FileName)
            # 直接删除文件
        else:
            powerRmDir(FileName)
            # 对文件夹先清空其下的文件再删除
    os.rmdir(path)
    # 在清空目录下的文件及文件夹后删除