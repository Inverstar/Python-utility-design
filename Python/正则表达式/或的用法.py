import re
m = '(a|b\d)|c'
# k = re.finditer(m,'abcdafab4c')
# print(k.groups())
for x in re.finditer(m,'abcdafab4c'):
    print(x.group())

m = '\[(\d+)\]|<(\d+)>'
for x in re.finditer(m,'233[32]88ab<433>'):
    print(x.group(),x.groups())
#group()是匹配的正则子串
#groups() 是分组匹配的内容子串

p='''bottle\r\nbag\r\nbig\napple'''

regex=re.compile(r'\bb(?P<middle>\w)(?P<tail>g)')
mat=regex.finditer(p)
print(mat)
for m in mat:
    print(m.groups()) # 匹配到的所有分组(包括命名分组)
    # print(m.group()) # m.group() == m.group(0) 匹配到的所有内容,与分组无关
    print(m.group())
    print(m.group(1))
    print(m.group(2))
    print(m.groupdict())