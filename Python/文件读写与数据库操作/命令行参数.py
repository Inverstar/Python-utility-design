# 命令行参数
# python 链.py a1.txt a2.txt
# 获取命令行参数
import sys
for x in enumerate(sys.argv):
    print(x)
print(sys.argv)
# sys.argv 是字符串列表