#给定n行m列的图像各像素点的灰度值，要求用如下方法对其进行模糊化处理：
#1. 四周最外侧的像素点灰度值不变；
#2. 中间各像素点新灰度值为该像素点及其上下左右相邻四个像素点原灰度值的平均（舍入到最接近的整数）。
import copy
n, m = map(int,input().split())
a = []
for i in range(n):
    lst = list(map(int,input().split()))
    a.append(lst)
b = copy.deepcopy(a)
for i in range(1,n-1):
    for j in range(1,m-1):
        b[i][j] = round((a[i][j] + a[i-1][j] + a[i+1][j] + a[i][j-1] + a[i][j+1])/5)
        # round(float) 四舍五入

for i in range(n):
    for j in range(m):
        print(b[i][j],end=' ')
    print()