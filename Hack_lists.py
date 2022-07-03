def ins(val):
    arr.insert(int(val[1]),int(val[2]))

def prt():
    print(arr)

def rem(val):
    arr.remove(int(val))

def app(val):
    arr.append(int(val))

def st():
    arr.sort()

def pp():
    arr.pop(-1)

def rev():
    arr.reverse()

if __name__ == '__main__':
    N = int(input())
    arr=[]
    for i in range(N):
        cmd=input("""Print your comamnd: """)
        comand=cmd.split()
        if comand[0].lower() == "insert":
            ins(comand)
        elif comand[0].lower() == "print":
            prt()
        elif comand[0].lower() == "remove":
            rem(comand[1])
        elif comand[0].lower() == "append":
            app(comand[1])
        elif comand[0].lower() == "sort":
            st()
        elif comand[0].lower() == "pop":
            pp()
        elif comand[0].lower() == "reverse":
            rev()
