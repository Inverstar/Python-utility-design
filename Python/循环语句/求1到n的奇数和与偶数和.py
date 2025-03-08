n = int(input())
m = int(input())
#-3 -2 -1 1 2 3
#-3 -2 4 2
奇数和 = 0
偶数和 = 0
if m > n:
    n, m = m, n
for x in range(m,n+1):
    if x%2 == 0:
        偶数和 += x
    else:
        奇数和 += x
print(奇数和, 偶数和)