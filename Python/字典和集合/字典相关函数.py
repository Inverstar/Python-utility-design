d = {1:89,2:11}
# 字典d
i = 1
if i in d:
    print(i,d)
print(d.items())
    #注意对字典本身使用in时，只能找到键，不能对其内容使用in
# 输出字典
for i in d.keys():
    print(i)
print(d.keys())
for i in d.values():
    print(i)
print(d.values())
for i in d.items():
    print(i)
for i,j in d.items():
    print(i,j)
#元素序列, 用于遍历
a = d.copy()

d.pop(1)
#删除键为1的元素, 不存在则产生异常


for i in a.items():
    # 如果有值为89的则输出
    if 89 == i[1]:
        print(i)
d.clear()
print(d)