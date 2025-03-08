a = [111,251,960,-12,-20]
b = sorted(a)
#sorted(a,reverse = True)
a.sort()
# a.sort(reverse = True)
print(a)
print(b)

def myKey(x):
    return x % 10
a.sort(key = myKey)
print(a)
print(-12%10 == 10-12%10)
#对负数-a, 取b-a%b