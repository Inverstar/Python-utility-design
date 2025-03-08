import sqlite3
db = sqlite3.connect('sqltest.db')
cur = db.cursor()
# 获取光标, 操作数据库一般通过光标进行
sqlcmd = \
"""
create table if not exists students
(id integer primary key, name text, gpa real, birthday date, age integer, picture blob)
"""
cur.execute(sqlcmd)
mylist = \
[(1700,'李四','3.25','2001-12-01',17,None),
 (1800,'王四','3.35','2000-12-01',18,None)]
for s in mylist:
    cur.execute('Insert into students values(?,?,?,?,?,?)',
                            (s[0],s[1],s[2],s[3],s[4],s[5]))
db.commit()
# 提交
cur.close()
# 关闭光标
db.close()
# 关闭数据库