n=int(input())
for i in range(n):
    x,y=map(int, input().split())
    try:
        d=x/y
        print(d)
    except Exception:
        print("divisao impossivel")
