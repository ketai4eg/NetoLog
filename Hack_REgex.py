import re
def choice(match):
    if match.group()=="&&":
        return "and"
    else:
        return "or"
N=input()
n=[]
for i in range(int(N)):
    line=input()
    n.append(line)
for i in n:
    print(re.sub(r"(?<= )(&&|\|\|)(?= )", choice, i))

