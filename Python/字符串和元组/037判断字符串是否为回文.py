# 输入一个字符串，输出该字符串是否回文。回文是指顺读和倒读都一样的字符串。
s = input()
for x in range(len(s)):
    if s[x] == s[-(x+1)]:
        if x == len(s) - 1:
            print('yes')
        continue
    else:
        print('no')
        break
# 切片
def 回文():
    s = input()
    x = s[::-1]
    if x == s:
        print('yes')
    else:
        print('no')
# 回文()
        