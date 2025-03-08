# i = 0
# while i<26:
#     print(chr(ord('a')+i))
#     i+=1
# while(input()!='pku'):
#     print('错误')
# else:
#     print('正确')
# 三个整数的最小公倍数
s = input().split()
x,y,z = int(s[0]),int(s[1]),int(s[2])
n = m = max(x,y,z)
while True:
    if n % x == 0 and n % y == 0 and n % z == 0:
        print(n)
        break
    n += m

