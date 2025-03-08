import datetime
weekdays = 1,2,3,4,5,6,7
s = input().split()
y,m,d = int(s[0]),int(s[1]),int(s[2])
dt = datetime.date(y,m,d)
print(weekdays[dt.weekday()])