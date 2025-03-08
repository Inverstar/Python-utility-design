#选择排序
def selectionSort(a):
    n  = len(a)
    for i in range(n-1):
        for j in range(i+1,n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
lst = [1,52,47,99,-7,-3,-5]
# 如何使用列表推导式生成随机序列?
print(lst)
selectionSort(lst)
print(lst)
# 归并排序, 快速排序, O(nlogn)

"""利用max或min实现选择排序"""
def mselectionSort(a):
    n = len(a)
    for i in range(n):
        j = a.index(min(a[i:]))
        if i == j:
            continue
        else:
            a[i], a[j] = a[j], a[i]
lst = [1,52,47,99,-7,-3,-5]
# 如何使用列表推导式生成随机序列?
print(lst)
mselectionSort(lst)
print(lst)

# python函数源码查看
# import inspect
# inspect.getdoc(BeautifulSoup)
# inspect.getsourcefile(BeautifulSoup)
# inspect.getsourcelines(BeautifulSoup)
# import dill
# dill.source.getsourcelines(BeautifulSoup)
# dill.source.findsource(BeautifulSoup)