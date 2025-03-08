"匹配对象的函数"
import re

h = re.compile(r'(\d)n.*(\d)n')
for k in h.finditer('45n 11n'):
    print(k.group(0,1,2))
    print(k.start(),k.end())
    print(k.span())
# span() = (start(),end()) 返回子串的起始索引
m = re.match(r'(\w+) (\w+)(.)','hello world!ss')
print(m.lastindex)
print(m.string)
print(m.groups())
print(m.start(2))
print(m.end(2))
# groups() == group(1,2,...,last)
