#upper, lower title
#find, rfind, index, rindex
#r倒着找
s = '12a4a15a1456a'
# print(s.rfind('a'))
try:
    s.rindex('3')
except Exception as e:
        print(e)
# print(s.find('a',3))
#指定从s[3]开始找
a = 0
for x in range(len(s)):
    s.find('a',a)
    if s.find('a',a) == -1:
        break
    else:
        print(s.find('a',a))
        a = s.find('a',a)+1
#replace(x,y)
#isdigit(),islower(),isupper()
#startswith(x),endswith(x)

#去空白字符(含转义)
#strip() lstrip() rstrip()
c = '14156151'
c = c.strip('15')
print(c)
"""
    对两端出现的选定字符进行去除
    直到两端字符均不是选定字符
"""

        