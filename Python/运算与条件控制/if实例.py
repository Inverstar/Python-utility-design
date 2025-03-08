#字符串切片 - 子串
# a = "abcdefg"
# print(a[2:-1])
# print(a[2:])

#温度转换
tmpStr = input()
if tmpStr[-1] in ['F','f']:
    C = ((float(tmpStr[0:-1]))-32)/1.8
    print("转换成"+str(C)+'C')
elif tmpStr[-1] in "Cc":
    F = 1.8 * eval(tmpStr[0:-1])+32
    print("转换成"+str(F)+'F')
else:
    print("非法输入")
