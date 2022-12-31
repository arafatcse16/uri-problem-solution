n=int(input())
value_in=0
value_out=0
for i in range(n):
    value=int(input())
    if value>=10 and value<=20:
        value_in+=1
    else:
        value_out+=1
print("{} in".format(value_in))
print("{} out".format(value_out))
