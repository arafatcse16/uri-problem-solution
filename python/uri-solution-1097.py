J=7
for i in range(1,10,2):
    temp=J
    for j in range(3):
        print("I={} J={}".format(i,temp))
        temp-=1
    J+=2
