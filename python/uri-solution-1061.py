dia,begi_dia=input().split()
begi_dia=int(begi_dia)
begi_hora, begi_minuto, begi_segundo=map(int, input().split(" : "))

dia,finsh_dia=input().split()
finsh_dia=int(finsh_dia)
finsh_hora, finsh_minuto, finsh_segundo=map(int, input().split(" : "))

Z=finsh_segundo-begi_segundo
Y=finsh_minuto-begi_minuto
X=finsh_hora-begi_hora
W=finsh_dia-begi_dia

if Z<0:
    Z+=60
    Y-=1
if Y<0:
    Y+=60
    X-=1
if X<0:
    X+=24
    W-=1

print("{} dia(s)".format(W))
print("{} hora(s)".format(X))
print("{} minuto(s)".format(Y))
print("{} segundo(s)".format(Z))
