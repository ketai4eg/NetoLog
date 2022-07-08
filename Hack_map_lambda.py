cube = lambda x: x**3

def fibonacci(n):
    if n==0:
        return[]

    elif n==1:
        return [0]
    else:
        start=[0,1]
        for i in range(2,n):
            start.append((start[i-2]+start[i-1]))
        return start
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))