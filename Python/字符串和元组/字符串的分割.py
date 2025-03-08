import re
"""
re高级分割
"""
# 使用多个分隔串进行分割
a = 'long*long-ago,a beautiful0girl@chang e'
a = '大福大|范德萨|的'
#[\u4e00-\u9fa5]
a = re.split('"|"',a)
# a = re.split('\.',a)
print(a)
# print(re.split('\\|/|.|//',a)[0])
# 为什么*之前要加\?
s = '12...34..56...a'
x = '..'
print(s.split(x))
#相邻的分隔符之间会分出空串
