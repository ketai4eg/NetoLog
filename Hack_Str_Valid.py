if __name__ == '__main__':
    s = input()
    First=False
    Second=False
    Third=False
    Forth=False
    Fifth=False
    for i in s:
        if i.isalnum():
            First=True
        if i.isalpha():
            Second=True
        if i.isdigit():
            Third=True
        if i.islower():
            Forth=True
        if i.isupper():
            Fifth=True
    print(First)
    print(Second)
    print(Third)
    print(Forth)
    print(Fifth)