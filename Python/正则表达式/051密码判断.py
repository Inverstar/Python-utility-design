import re
m='[A-Za-z][-A-Za-z0-9_]{7,}\Z'
while True:
    try:
        s = input()
        if re.match(m,s) != None:
            print("yes")
        else:
            print("no")
    except:
        break
