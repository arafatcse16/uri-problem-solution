n=int(input())
odd=[]
for i in range(n):
    temp_sum=0 
    x,y=map(int,input().split())
    if x==y:
      odd.append(0)  
    elif x>y:
        for j in range(y+1,x):
            if j%2!=0:
                temp_sum+=j
        odd.append(temp_sum)
    elif y>x:
        for j in range(x+1,y):
            if j%2!=0:
                temp_sum+=j
        odd.append(temp_sum)
for i in range(len(odd)):
    print(odd[i])
