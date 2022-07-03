def full_list(elements):
    allnum = []
    for i in range(0, int(elements)):
        num = input("Give your num: ")
        allnum.append(num)
    return allnum

def printing(allnum):
    allnum.sort()
    print(f"max: {allnum[len(allnum) - 1]}, min: {allnum[0]}")

def final(allnum):
    if len(set(allnum))==1:
        print("All numbers are the same!!!")
    elif len(allnum) != len(set(allnum)):
        print(f"There is {(len(allnum) - len(set(allnum))) + 1} identical numbers")
        printing(allnum)
    else:
        printing(allnum)

allnum=full_list(input("how much numbers you want to compare: "))

final(allnum)