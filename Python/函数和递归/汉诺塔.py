def Hanoi(n,src,mid,dest):
    if n == 1:
        print(src + '->'+dest)
        return
    Hanoi(n-1,src,dest,mid)
    print(src+"->"+dest)
    Hanoi(n-1,mid,src,dest)
n = int(input())
Hanoi(n,'A','B','C')

#2**n - 1