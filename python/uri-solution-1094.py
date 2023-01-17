n=int(input())
total,coel,rat,sap=0,0,0,0
for i in range(n):
    qty,ch=map(str,input().split())
    qty=int(qty)
    total+=qty
    if ch=='C':
        coel+=qty
    elif ch=='S':
        sap+=qty
    elif ch=='R':
        rat+=qty
print("Total: {} cobaias".format(total))
print("Total de coelhos: {}".format(coel))
print("Total de ratos: {}".format(rat))
print("Total de sapos: {}".format(sap))
coel=(coel*100)/total
print("Percentual de coelhos: {:.2f} %".format(coel))
rat=(rat*100)/total
print("Percentual de ratos: {:.2f} %".format(rat))
sap=(sap*100)/total
print("Percentual de sapos: {:.2f} %".format(sap))
