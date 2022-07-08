m, n =input().split()
for i in range(1,int(m)+1,2):
    if i<(int(m)):
        print(f"{'-' * int(((int(n)-3*(i))/2))}{'.|.' * (i)}{'-' * int(((int(n)-3*(i))/2))}")
    elif i==(int(m)):
        print(f"{'-'*int((int(n)-7)/2)}WELCOME{'-'*int((int(n)-7)/2)}")
for i in range(int(m)-2, 0, -2):
    print(f"{'-' * int(((int(n) - 3 * (i)) / 2))}{'.|.' * (i)}{'-' * int(((int(n) - 3 * (i)) / 2))}")
