#有三个字符串S,S1,S2，其中，S长度不超过300，S1和S2的长度不超过10。想检测S1和S2是否同时在S中出现，且S1位于S2的左边，并在S中互不交叉（即，S1的右边界点在S2的左边界点的左侧）。计算满足上述条件的最大跨距（即，最大间隔距离：最右边的S2的起始点与最左边的S1的终止点之间的字符数目）。如果没有满足条件的S1，S2存在，则输出-1。 
s = input().split(',')
S, S1, S2= s[0], s[1], s[2]
if S1 not in S or S2 not in S:
    print(-1)
else:
    z = S.find(S1)
    y = S.rfind(S2)
    k = y-z-len(S1)
    if k>=0:
        print(k)
    else:
        print(-1)