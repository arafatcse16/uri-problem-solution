product1=input().split()
product2=input().split()
product1_price=float(product1[1])*float(product1[2])
product2_price=float(product2[1])*float(product2[2])
total_paid=product1_price+product2_price
print("VALOR A PAGAR: R$ %.2f"%total_paid)
