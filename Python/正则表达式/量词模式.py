import re
m = 'a.*b'
# 贪婪模式
'量词+,*,?,{m,n}'# : #'默认匹配尽可能长的子串'
for k in re.findall(m,'aabab'):
    print('贪',k)


m = "a.*?b"
# 懒惰模式
'在+,*,?,{m,n}后加?'
for k in re.findall(m,'aabab'):
    print(k)
