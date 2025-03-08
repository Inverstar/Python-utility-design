#输入3个数求和
#9b16bd7e5a5e63d1bddbdef913a20868c0380eb3a7403442b250a81fb1895660
a = input()
a = a.split()
b = 0
for x in a:
    b += float(x)
print(b)