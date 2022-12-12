pi=3.14159
lst=list(map(float, input().split()))
A=lst[0]
B=lst[1]
C=lst[2]
triangle=(A*C)/2
print("TRIANGULO: %.3f"%triangle)
circle=pi*C*C
print("CIRCULO: %.3f"%circle)
trapezium=((A+B)/2)*C
print("TRAPEZIO: %.3f"%trapezium)
square=B*B
print("QUADRADO: %.3f"%square)
rectangle=A*B
print("RETANGULO: %.3f"%rectangle)
