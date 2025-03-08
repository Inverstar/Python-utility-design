import jieba as j
# pip -V
# pip show jieba
# pip list
# https://www.piqizhu.com/

s = '某些时候可能会觉得有点点难过'
s1 = j.lcut(s)
# 默认精确模式分词
print(j.lcut(s,cut_all = True))
# 全模式分词, 输出所有可能的词
print(j.lcut_for_search(s))
# 搜索引擎模式分词
# 向词典添加新词
# 添加是临时性的
j.add_word('拼多多')
print(j.lcut('拼多多真的便宜'))

j.load_userdict('玩转Python生态/tmpdict.txt')
print(j.lcut('维斯坦星巴克瑞幸'))