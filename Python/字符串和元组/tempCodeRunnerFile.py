x = (1,2,3) * 3 # *像是连加号
print(x)
for i in x:
    print(i,end = '')
b = x
print('\n',b is x)
x += (100,)
print(x is b)