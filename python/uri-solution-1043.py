a,b,c=map(float, input().split())
if ((a+b)>c and (b+c)>a and (c+a)>b):
    perimeter=a+b+c
    print("Perimetro = %.1f"%perimeter)
else:
    area=.5*(a+b)*c
    print("Area = %.1f"%area)
