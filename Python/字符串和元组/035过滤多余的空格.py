#一个句子中也许有多个连续空格，过滤掉多余的空格，只留下一个空格。
s = input().split()
s = ' '.join(s)
print(s)