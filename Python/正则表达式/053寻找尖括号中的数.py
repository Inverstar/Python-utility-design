n=int(input())
import re
for i in range(n):
    s=input()
    m='<(0|[1-9][0-9]{0,2})>'
    result=re.findall(m,s)
    if result==None:
        print("NONE")
    elif len(result)==0:
        print("NONE")
    else:
        for x in result:
            print(x,end=" ")
        print("")
