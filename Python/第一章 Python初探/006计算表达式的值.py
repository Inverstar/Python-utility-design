#输入仅一行，包括三个整数a、b、c, 数与数之间以一个空格分开。
#(－10,000 < a,b,c < 10,000)
#f40e006b5122a042552c80be35f9f933950cb64a21a7a0458e8bef595190a5df
s = input().split()
a,b,c = int(s[0]),int(s[1]),int(s[2])
print((a+b)*c)