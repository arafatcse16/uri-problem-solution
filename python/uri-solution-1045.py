a,b,c=map(float, input().split())
if a>=(b+c) or b>=(a+c) or c>=(a+b):
    print("NAO FORMA TRIANGULO")
elif a*a==(b*b+c*c) or b*b==(a*a+c*c) or c*c==(b*b+a*a):
    print("TRIANGULO RETANGULO")
elif a*a>(b*b+c*c) or b*b>(a*a+c*c) or c*c>(b*b+a*a):
    print("TRIANGULO OBTUSANGULO")
elif a*a<(b*b+c*c) or b*b<(a*a+c*c) or c*c<(b*b+a*a):
    print("TRIANGULO ACUTANGULO")
if a==b==c:
    print("TRIANGULO EQUILATERO")
elif a==b or a==c or b==c:
    print("TRIANGULO ISOSCELES")
