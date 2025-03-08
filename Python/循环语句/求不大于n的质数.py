n = int(input())
for i in range(3,n+1,2):
    ok = True
    for k in range(3,i,2):
        if i % k == 0:
            ok = False
            break
        if k*k>i:
            break
    if ok:
        print(i)