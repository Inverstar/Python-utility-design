#输入两个串s1,s2，找出s2在s1中所有出现的位置
#两个子串的出现不能重叠。例如'aa'在 aaaa 里出现的位置只有0,2
n = int(input())
for x in range(n):
    s = input().split()
    a = 0
    for x in range(len(s[0])):
        s[0].find(s[1],a)
        if s[0].find(s[1],a) == -1:
            if x == 0:
                print('no',end=' ')
            break
        else:
            print(s[0].find(s[1],a),end=' ')
            a = s[0].find(s[1],a)+len(s[1])
    print()