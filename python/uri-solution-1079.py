n = int(input())
wght_avg=[]
for i in range(n):
    x,y,z=map(float, input().split())
    wght_avg.append(((x*2)+(y*3)+(z*5))/(2+3+5))

for i in range(len(wght_avg)):
    print("%.1f"%wght_avg[i])
