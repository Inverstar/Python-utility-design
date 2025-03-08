#给定三个正整数m,n,s问从1到m这m个数里面取n个不同的数，使它们和是s,有多少种取法
#076d793f05299d9adbe9e5d74b86171a421882447b6b348fd1f47e315addaa2e
def ways(m,n,s):
    if n == 0 :
        return 1 if s==0 else 0
    if m < n or m == 0:
        return 0
    if m > s:
        return ways(s,n,s)
    else:
        return ways(m-1,n-1,s-m)+ways(m-1,n,s)
        # 取走m和不取走m的办法！
s = int(input())
for x in range(s):
    k = input().split()
    k = [int(j) for j in k]
    print(ways(k[0],k[1],k[2]))

