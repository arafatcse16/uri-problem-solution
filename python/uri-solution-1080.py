j=0
for i in range(100):
    x=int(input())
    if x>j:
        temp=i+1
        j=x
print(j)
print(temp)
