# n = int(input())
# total = 0
# for x in range(n):
#     total += int(input())
# print(total)

n = int(input())
for x in range(1,n+1):
# for x in range(n,0,-1):
    if n % x == 0:
        #输出因子
        print(x,end=' ')
# 多重循环取数
total = 0
lst = input().split()
n, m = int(lst[0]), int(lst[1])
for i in range(1,n):
    for j in range(i+1, n+1):
        if m % (i+j) == 0:
            print(i, j)
            total += 1
print(total)
