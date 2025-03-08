dict1 = {}
while True:
    try:
        n = int(input())
        dict1[n] = dict1.get(n,0) + 1
    except:
        break
list1 = []
for x in dict1.items():
    list1.append(x)
list1.sort(key = lambda x : x[1])
a = list1[0][1]
for x in list1:
    if x[1] == a:
        print(x)
    else:
        break
