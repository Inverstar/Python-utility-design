import datetime
while True:
    try:
        a=input()
        if "AM" in a or "PM" in a:
            tm1=datetime.datetime.strptime(a,"%m-%d-%Y %H:%M %p") # 生成时间对象
        else:
            tm1=datetime.datetime.strptime(a,"%Y %m %d %H %M")
        b=input()
        if ' ' not in b:
            delta=datetime.timedelta(seconds=int(b))
        else:
            i,j,k=map(int,b.split())
            delta=datetime.timedelta(days=i,hours=j,minutes=k)
        newt=tm1+delta

        print(newt.strftime("%Y-%m-%d %H:%M:%S"))
    except  Exception as a:
        break
