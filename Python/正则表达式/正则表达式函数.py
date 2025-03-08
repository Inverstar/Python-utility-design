import re
# re.match(pattern, string, flags=0)
# flag 标志位, 匹配控制模式
#   re.M 多行匹配, 影响^与$
#   re.S 使.匹配包括换行符的所有字符
#   re.I 忽略大小写
#   re.U 根据Unicode字符集解析字符,影响\w,\W,\b,\B
#   re.X 灵活模式? 
"""
re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
re.search匹配整个字符串，直到找到一个匹配
"""
def match(pattern,string):
    x = re.match(pattern,string)
    if x != None:
        print(x.group())
    else:
        print(x)
match('a c','a cdjfia')
def search(pattern,string):
    x = re.search(pattern,string)
    if x != None:
        print(x.group(),x.span())
    else:
        print(x)
search("a.*b","abadfbdafsfb")
# re.findall 找出所有可匹配的无重复结果列表
print(re.findall('\d+',"this is 43 that 33"))
# re.finditer(pattern, string, flags = 0)
# 返回匹配对象序列(可调用迭代器)
s = "dasfsfhu39048293df"
m = '\d|\s'
for x in re.finditer(m,s):
    print(x.group(),x.span())
listx = [x.group() for x in re.finditer(m,s)]
print(listx)
#re.sub 替换匹配的子串
#re.sub(pattern,替换串,string)
s1 = re.sub('[a-z]',' ',s)
print(s1)