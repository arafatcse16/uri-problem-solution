x,y=map(int, input().split())
price=[4.00,4.50,5.00,2.00,1.50]
pay=price[x-1]*y
print("Total: R$ %.2f"%pay)
