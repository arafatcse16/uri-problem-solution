n1, n2, n3, n4 = map(float, input().split())
average=(n1*2 + n2*3 + n3*4 + n4*1)/10
print("Media: %.1f"%average)
if average >=7:
    print("Aluno aprovado.")
elif average>=5 and average<7:
    print("Aluno em exame.")
    n5=float(input())
    print("Nota do exame: %.1f"%n5)
    re_average= (average+n5)/2
    if re_average >5:
        print("Aluno aprovado.")
        print("Media final: %.1f"%re_average)
    elif re_average<5:
        print("Aluno reprovado.")
        print("Media final: %.1f"%re_average)
    
else:
    print("Aluno reprovado.")
    
