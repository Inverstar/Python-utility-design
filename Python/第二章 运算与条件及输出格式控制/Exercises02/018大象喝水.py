#一只大象口渴了，要喝20升水才能解渴，
#但现在只有一个深h厘米，底面半径为r厘米的小圆桶(h和r都是整数)。
#问大象至少要喝多少桶水才会解渴。
#b6ff1a51b2c1363ae3f15217c22e8c0da2c1c901bea7cc3b2cb94aa6166bb2ce
s = input().split()
t = 3.14159*eval(s[1]+"**"+'2'+'*'+s[0])
if 20000%t == 0:
    print(int(20000//t))
else:
    print(int(20000//t+1))