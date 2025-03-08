#给定一个长度为n的非负整数序列，请计算序列的最大跨度值（最大跨度值 = 最大值减去最小值）。
#b0da7057882ccc580b25849f3a4956e6e0aa282262a095d5153829d54920a8a0
n = input()
s = input().split()
maxV = minV = int(s[0])
for x in s:
    if maxV < int(x):
        maxV = int(x)
    minV = min(minV,int(x))
print(maxV-minV)