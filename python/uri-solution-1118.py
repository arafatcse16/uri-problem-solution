import sys

temp=0
avg=0
while True:
    n=float(input())
    if n<0 or n>10:
        print("nota invalida")
    else:
        temp+=1
        avg+=n
        if temp==2:
            temp=0
            avg/=2
            print("media = %.2lf" %avg)
            avg=0
            while True:
                x=int(input())
                print("novo calculo (1-sim 2-nao)")
                if x==1:
                    break
                elif x==2:
                    sys.exit()
