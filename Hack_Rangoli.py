def lines_final( line:str, lenght_max:int)->str:
    return line.center(lenght_max,"-")



def lines(main_line):
    m_list=list(main_line)
    # print("-".join(m_list))
    return "-".join(m_list)

def print_rangoli(size):
    alpha='abcdefghijklmnopqrstuvwxyz'
    final_list=[]
    x=size-1
    lenght_max=len(lines(f"{alpha[size-1:0:-1]}{alpha[0:size]}"))
    # print(lenght_max)
    for i in range((size-1),0,-1):
        final_list.append(lines_final(lines(f"{alpha[size-1:0+x:-1]}{alpha[0+x:size]}"), lenght_max))
        if x>0:
            x-=1
    for i in range((size),0,-1):
        final_list.append(lines_final(lines(f"{alpha[size-1:0+x:-1]}{alpha[0+x:size]}"), lenght_max))
        x+=1
    print("\n".join(final_list))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)