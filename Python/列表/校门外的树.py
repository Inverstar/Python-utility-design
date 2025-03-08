s = input().split()
L, M = int(s[0]), int(s[1])
tree = [1] * (L+1)
for i in range(M):
    s = input().split()
    q, z = int(s[0]), int(s[1])
    for k in range(q,z+1):
        tree[k] = 0
print(sum(tree))