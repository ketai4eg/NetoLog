if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr_l=list(arr)
    arr_l.sort(reverse=True)
    first=arr_l[0]
    for a in arr_l:
        if first!=a:
            print(a)
            break