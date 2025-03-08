#给定一个只包含小写字母的字符串，请你找到第一个仅出现一次的字符。如果没有，输出no。
s = input()
for i in range(len(s)):
    if s[i] not in s[0:i]:
        if s[i] not in s[i+1:]:
            print(s[i])
            break
else:
    print('no')