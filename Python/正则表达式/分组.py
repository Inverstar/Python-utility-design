import re
x = re.search('[a-z]+(\d+)[a-z]+',"dsaf089d99fd1a9")
x = re.match('[a-z]+(\d+)[a-z]',"dsaf089d99fd1a9")
print(x.groups())
print(x.group(0))
print(x.group(1))
#分组
m = r'(((ab*)c)d)e\3'   #分组右边\n(n是数字, 即本次匹配的第几个分组所匹配的子串)
r = re.match(m,"abbbcdeabbbkfg")
for i in r.groups():
    print(i)
# 分组作为整体可跟量词
# findall 与 分组

"1 正则表达式没有或只有一个分组时"
# re.findall 返回所有匹配子串或分组子串的列表

m = 'a(.)a'
x = re.findall(m,'dafaa\nagaa啊a的方式',re.S)
print(x)

"2 多个分组时, 返回元组列表, 每个元组对应包含所有分组匹配的子串"
m = '(\w+) (\w+)'
r = re.search(m,"hello world")
print(r.groups())
r = re.findall(m,"hello world, this is very good")
print(r)