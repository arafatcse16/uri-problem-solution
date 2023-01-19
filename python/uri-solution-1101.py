while True:
    m, n = map(int, input().split())
    x=min(m,n)
    y=max(m,n)
    if n<=0 or m<=0:
        break
    else:
        S=0
        for j in range(x,y+1):
            S+=j
            print(j,end=' ')
        print("Sum={}".format(S))
