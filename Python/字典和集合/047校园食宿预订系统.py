"""

某校园为方便学生订餐，推出食堂预定系统。
食宿平台会在前一天提供菜单，学生在开饭时间前可订餐。 
食堂每天会推出m个菜，每个菜有固定的菜价和总份数，售卖份数不能超过总份数。 
假设共有n个学生点餐，每个学生固定点3个菜，当点的菜售罄时, 学生就买不到这个菜了。 
请根据学生预定记录，给出食堂总的预定收入 数据满足1 <= n <= 6000，3 <= m <= 6000，单品菜价不大于1000元，每个菜的配额不超过3000

"""
#输入两个整数n和m，代表有n个学生订餐，共有m个可选的菜
n,m=map(int,input().split())
#下面m行，每行三个元素，分别是菜名、售价和可提供量，保证菜名不重合，菜价为整数
menu={}
for i in range(m):
    arry=input().split()
    dish_name,selling_price,total=arry[0],int(arry[1]),int(arry[2])
    menu[dish_name]=(selling_price,total)

reservation={}
#下面n行，每行三个元素，表示这个学生点的三个菜的菜名
for i in range(n):
    for dish in input().split():
        reservation[dish]=reservation.get(dish,0)+1
income=0
for dish in reservation.items():
    if dish[0] in menu:
        income+=menu[dish[0]][0]*(min(menu[dish[0]][1],dish[1]))
print(income)