dict1 = {}
while True:
    try:
        wd = input()
        # if wd in dict:
        #     dict1[wd] +=1
        # else:
        #     dict1[wd] = 1
        dict1[wd] = dict1.get(wd,0) + 1
    except:
        break
result = []
# 字典不可排序, 所以要将每一项化为元组再添加入列表进行排序
for x in dict1.items():
    result.append(x)
result.sort(key = lambda x : (-x[1],x[0]))
for x in result:
    print(x[1],x[0])