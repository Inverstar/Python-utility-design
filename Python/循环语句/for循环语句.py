for x in range(3,12,3):
    print(x,' ',end='')
else:
    print('结束')
"""
字符编码
ord(x) 求字符x的编码
chr(x) 求编码为x的字符
"""
for i in range(26):
    print(chr(ord('a')+i),end=' ')
print('完毕')
# for循环遍历列表
a = 'Google'
for i in range(len(a)):
    if a[i] == 'o':
        continue
    print(i,a[i])
for i in a:
    print(i,end='')
    if i == 'o':
        break
