def mutate_string(string:str, position=0, character="A")-> str:
    str_list=list(string)
    str_list[position]=character
    res="".join(str_list)
    return res

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)