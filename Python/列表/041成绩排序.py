#给出班里某门课程的成绩单，请你按成绩从高到低对成绩单排序输出，如果有相同分数则名字字典序小的在前。
n = int(input())
a = []
for i in range(n):
    s = input().split()
    a.append((s[0],int(s[1])))
a.sort(key = lambda x: (-x[1],x[0]))
for x in a:
    print(x[0],x[1])