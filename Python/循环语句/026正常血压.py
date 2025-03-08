#监护室每小时测量一次病人的血压，若收缩压在90 - 140之间并且舒张压在60 - 90之间（包含端点值）则称之为正常，现给出某病人若干次测量的血压值，计算病人保持正常血压的最长小时数。
#ec973f35090ad5f19e1960b7780855629008880bdd50f2c05c9b126d64f82cb7
n , i, h= int(input()) , 0, 0
while n:
    n -= 1
    XY = input().split()
    X , Y= int(XY[0]),int(XY[1])
    if 90<= X <=140 and 60<= Y <=90:
        i += 1
        if n == 0 and i>h:
            h=i
    else:
        if i>h:
            h = i
        i = 0
print(h)