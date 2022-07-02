if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    cub=[]
    res=[]
    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range(0,z+1):
                cub.append([i,j,k])
    for el in cub:
        if sum(el)!=n:
            res.append(el)
    print(res)
