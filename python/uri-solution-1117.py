temp=0
avg=0
while True:
    x=float(input())
    if x<0 or x>10:
        print("nota invalida")
    else:
        temp+=1
        avg+=x
        if temp==2:
            avg/=2
            print("media = %.2f" %avg)
            break
