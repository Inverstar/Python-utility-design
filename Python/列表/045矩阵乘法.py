#计算两个矩阵的乘法。n*m阶的矩阵A乘以m*k阶的矩阵B得到的矩阵C 是n*k阶的，且C[i][j] = A[i][0]*B[0][j] + A[i][1]*B[1][j] + …… +A[i][m-1]*B[m-1][j](C[i][j]表示C矩阵中第i行第j列元素)。
n,m,k = map(int,input().split())
a,b,c = [],[],[]
print(c)
for i in range(n):
        a.append(list(map(int,input().split())))
for i in range(m):
        b.append(list(map(int,input().split())))
for i in range(n):
    c.append([])
    for j in range(k):
        c[i].append(0)
        for v in range(m):
            c[i][j] += a[i][v]*b[v][j]
for i in range(n):
    for j in range(k):
        print(c[i][j],end = ' ')
    print()