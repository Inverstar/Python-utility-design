#一个十进制自然数,它的七进制与九进制表示都是三位数，且七进制与九进制的三位数码表示顺序正好相反。编程求此自然数,并输出显示。
#be8b8f979ab15aacf7d1e56c935c448800096ce9b7625791830588ccf29a0af4
for x in range(81,553):
    if x%7 == x//81:
        x1 = str(x%7)
        if x//7%7 == x//9%9:
            x2 = str(x//7%7)
            if x//49 == x%9:
                x3 = str(x//49)
                print(x)
                print(x3+x2+x1)
                print(x1+x2+x3)
                break
    