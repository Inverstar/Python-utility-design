"""
有一个正方形，四个角的坐标（x,y)
分别是（1，-1），（1，1），（-1，-1），（-1，1），
x是横轴，y是纵轴。写一个程序，判断一个给定的点是否在这个正方形内（包括正方形边界）。
"""
#3f50b2a9b980c48dc41fe0fc4dbc525a8d1b2a5415b76461fd4cd4f4348d99d7
zuobiao = input().split()
if -1<=int(zuobiao[0])<=1:
    if -1<=int(zuobiao[1])<=1:   
        print('yes')
    else:
     print('no')
else:
     print('no')
