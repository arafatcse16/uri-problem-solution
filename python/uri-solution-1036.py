A,B,C = map(float,input().split())
d = B * B - 4 * A * C
e = pow(d, .5)
if (d < 0 or A == 0):
    print("Impossivel calcular")
else:
    r1 = (-B + e) / (2 * A)
    r2 = (-B - e) / (2 * A)
    print("R1 = %.5lf"%r1)
    print("R2 = %.5lf"%r2)
