import sqlite3
db = sqlite3.connect('sqltest.db')
cur = db.cursor()
sql = 'select * from students'
cur.execute(sql)

y = cur.fetchall()
# print(x,y)
for i in y:
    print(i)
sql = ("select * from students where name = 'jack'")
cur.execute(sql)
x = cur.fetchone()
if x == None:
    print('No jack')
sql = 'update students set gpa = ?, age = ? where name = ?'
cur.execute(sql,(1.0,30,'李四'))
db.commit()
sql = 'select * from students'
cur.execute(sql)
y = cur.fetchall()
for i in y:
    print(i)
cur.close()
db.close()
