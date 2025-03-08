#给定一个整数，请将该数各个位上数字反转得到一个新数。新数也应满足整数的常见形式，即除非给定的原数为零，否则反转后得到的新数的最高位数字不应为零（参见样例2）。
#ce547bd557e7175e90dc23d82a1125cd3fe778df4889ffce750864fbf9117529

n = int(input())
if n < 0:
    n = -n
    print('-',end='')
while n%10 == 0 and n != 0:
    n //= 10
n = str(n)
for x in range(-1,-len(n)-1,-1):
    print(n[x],end='')

