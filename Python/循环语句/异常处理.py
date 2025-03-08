"""
1. ArithmeticError 此基类用于派生针对各种算术类错误而引发的内置异常: OverflowError, ZeroDivisionError, FloatingPointError
2. BufferError 当与 缓冲区 相关的操作无法执行时将被引发。
3. LookupError 此基类用于派生当映射或序列所使用的键或索引无效时引发的异常: IndexError, KeyError。 这可以通过 codecs.lookup() 来直接引发
4. ImportError 当 import 语句尝试加载模块遇到麻烦时将被引发。 并且当 from ... import 中的 "from list" 存在无法找到的名称时也会被引发
5. IndexError 当序列抽取超出范围时将被引发。 （切片索引会被静默截短到允许的范围；如果指定索引不是整数则 TypeError 会被引发
"""
class NameTooShortError(ValueError): 
    pass
def validate(name):
    if len(name) < 10:
        raise NameTooShortError(name)
        
# 使用自定义异常类，使得发生异常时的错误更容易排查
s = input()
lst = s.split()
maxV = int(lst[0])
validate(s)
try:
    while True:
        lst = s.split()
        for x in lst:
            maxV = max(maxV,int(x))
        s = input() #ctrl+d
except:
    pass
print(maxV)