import sqlite3
import requests
# f = open('tmp.jpg','rb') 
# # 二进制打开图片
# img = f.read()
# f.close()
imgUrl = 'https://img.moegirl.org.cn/common/thumb/7/78/Royal_Bordello.jpg/200px-Royal_Bordello.jpg'
imgStream = requests.get(imgUrl, stream = True)
db = sqlite3.connect('sqltest.db')
cur = db.cursor()
sql = "update students set picture = ? where name = '李四' "
cur.execute(sql,(imgStream.content,))
# 多的逗号意味着元组