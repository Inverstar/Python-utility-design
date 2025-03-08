#给定年月日，求星期几。已知2020年11月18日是星期三。另外，本题有公元0年，这个和真实的纪年不一样
# 暂时不搞!!!
def cal(y,m,d):#计算给定日期和2020年1月1日的差距
    mdays = (-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    if y>=2020:
        days = 365 * (y - 2020) + (y -1- 2020) // 4 + sum(mdays[1:m]) + d
        if m > 2 and ((y % 4==0 and y % 100 != 0) or y % 400==0):
            days += 1
        days -= (y - 2000 - 1) // 100 - (y - 2000 - 1) // 400
    else:
        days=365 * (2020-y) + (2020-y) // 4
        # days-=(2000-y-1)//100-(2000-y-1)//400
        days -= (2000 - y ) // 100 - (2000 - y ) // 400
        days=-days
        days+=sum(mdays[1:m]) + d-1
        if m > 2 and ((y % 4==0 and y % 100 != 0) or y % 400==0):
            days += 1
    return days

def cal_weekdays(y,m,d):
    weekdays = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
    return weekdays[(cal(y,m,d)+3)%7]

def isIllegal(m,d):
    if (y % 4==0 and y % 100 != 0) or y % 400==0:
        mdays = (-1, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    else:
        mdays = (-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    if m not in range(1,13):
        return True
    else:
        if d not in range(1,mdays[m]+1):
            return True
        else:
            return False

n=int(input())
for count in range(n):
    s=input().split()
    y,m,d=int(s[0]),int(s[1]),int(s[2])
    if isIllegal(m,d):
        print("Illegal")
    else:
        print(cal_weekdays(y, m, d))