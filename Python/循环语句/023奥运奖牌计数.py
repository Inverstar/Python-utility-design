#2008年北京奥运会，A国的运动员参与了n天的决赛项目(1≤n≤17)。现在要统计一下A国所获得的金、银、铜牌数目及总奖牌数。
#8c3838ad123d3880d7ca0fcabdd8ec626d07efd6575247742611bccadcab37b5
n = int(input())
j = y = t = z = 0
while n:
    n -= 1
    s = input().split()
    j += int(s[0])
    y += int(s[1])
    t += int(s[2])
z = j+y+t
print(j,y,t,z)
