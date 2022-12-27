init_hour,init_mint,final_hour,final_mint=list(map(int,input().split()))

dif=((final_hour*60)+final_mint)-((init_hour*60)+init_mint)
if(dif<=0):
    dif+=24*60
    
time=dif//60
minute=dif%60
print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(time,minute))
