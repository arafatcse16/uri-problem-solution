alc=0
gas=0
disl=0
print("MUITO OBRIGADO")
while True:
    n=int(input())
    if n==1:
        alc+=1
    elif n==2:
        gas+=1
    elif n==3:
        disl+=1
    elif n==4:
        break
print("Alcool: {}".format(alc))
print("Gasolina: {}".format(gas))
print("Diesel: {}".format(disl))
