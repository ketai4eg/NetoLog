import re
S="aaadaa"
k=re.compile("aa")
m=k.search(S)
if m:
    while m:
        print((m.start(), m.end()-1))
        m=k.search(S, m.start()+1)
else:
    print((-1,-1))