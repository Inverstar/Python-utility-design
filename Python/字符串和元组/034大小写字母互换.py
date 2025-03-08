# 把一个字符串中所有出现的大写字母都替换成小写字母，同时把小写字母替换成大写字母。
s = input()
for c in s:
    if c.isalpha():
        if c.isupper():
            print(c.lower(),end='')
        else:
            print(c.upper(),end='')
    else:
        print(c,end='')
