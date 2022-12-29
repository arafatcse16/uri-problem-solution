even,odd,postive,negative=0,0,0,0
for i in range(5):
    n=int(input())
    if n==0:
        if n%2==0:
            even+=1
        else:
            odd+=1
    elif n>0:
        postive+=1
        if n%2==0:
            even+=1
        else:
            odd+=1
    elif n<0:
        negative+=1
        if n%2==0:
            even+=1
        else:
            odd+=1
            
print("{} valor(es) par(es)".format(even))
print("{} valor(es) impar(es)".format(odd))
print("{} valor(es) positivo(s)".format(postive))
print("{} valor(es) negativo(s)".format(negative))
