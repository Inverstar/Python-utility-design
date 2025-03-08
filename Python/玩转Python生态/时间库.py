# 只能处理公元1~公元9999年
import datetime as dt
import time as t
dtBirth = dt.date(1998,1,6)
dtToday = dt.date.today()
#创建日期对象 今天和生日
life = dtToday - dtBirth
# 时间差
print('活了:',life.days,'天',life.total_seconds(),'秒')
# 构造时间差对象
delta = dt.timedelta(seconds = 2700000000)
DieDay = dtBirth + delta
print(DieDay)
print(DieDay.strftime(r'%Y/%m/%d'))
print(DieDay.strftime(r'%D'))
print(dtBirth.weekday())
print(dtToday.weekday())
# 输出日期的星期, 从0到6,周一到周日

date1 = dt.datetime.strptime('2020.08.08','%Y.%m.%d')
print(date1.strftime('%Y%m%d\n'))

NOW = dt.datetime.now()
TM = dt.datetime(2060,8,10,15,34,23,1)
print(TM.strftime('%H:%M:%S'))
print(NOW.strftime('%I:%M:%S %p'))
print(t.ctime(t.time()))