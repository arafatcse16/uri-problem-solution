salary=float(input())
taxes=0
if salary<=2000:
    taxes=0
    print("Isento")
elif salary<=3000:
    taxes=(((salary-2000)*8)/100)
    print("R$ %.2f"%taxes)
elif salary<=4500:
    taxes=(((salary-2000)-(salary-3000))*8/100)+(((salary-3000)*18)/100)
    print("R$ %.2f"%taxes)
elif salary>4500:
    taxes=((1000*8)/100)+((1500*18)/100)+(((salary-4500)*28)/100)
    print("R$ %.2f"%taxes)
