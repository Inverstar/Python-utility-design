#给定三个正整数，分别表示三条线段的长度，判断这三条线段能否构成一个三角形。
#2e71701582f74af29545b4858e4cb52f2026d0e967525b4c4c187d63ed7c54fa
s = sorted(input().split())
# s = (input().split()).sort()
if eval(s[0]+'+'+s[1])>int(s[2]):
    print("yes")
else:
    print('no')
# list1 = list1.sort()