# 输入一行字符，统计出其中数字字符的个数。
s = input()
n = 0
for c in s:
    if c.isdigit():
        n += 1
print(n)