positive=0
average=0
for i in range(6):
    n=float(input())
    if n>0:
        positive+=1
        average+=n
print("{} valores positivos".format(positive))
print("%.1f"%(average/positive))
