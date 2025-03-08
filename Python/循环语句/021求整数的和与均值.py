#读入n（1 <= n <= 10000）个整数，求它们的和与均值。
#287c7e55348c756c321367881963607fe704f5ce72fc22dc3e2f77acab9c206e
n = int(input())
k = 0
for x in range(n):
    k += int(input())
print(k,end=' ')
print("%.5f"%(k/n))