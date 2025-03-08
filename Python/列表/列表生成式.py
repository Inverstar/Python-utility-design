print([x*x for x in range(1,11)])
print([m for m in 'ABC'])
L = ['a',1,'v',3]
print([s.lower() for s in L if isinstance(s,str)])
print(tuple(s.lower() for s in L if isinstance(s,str)))