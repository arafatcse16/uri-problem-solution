salary=float(input())
if salary<=400:
    money_earned=(salary*15)/100
    new_salary=money_earned+salary
    percentage=15
elif salary<=800:
    money_earned=(salary*12)/100
    new_salary=money_earned+salary
    percentage=12
elif salary<=1200:
    money_earned=(salary*10)/100
    new_salary=money_earned+salary
    percentage=10
elif salary<=2000:
    money_earned=(salary*7)/100
    new_salary=money_earned+salary
    percentage=7
elif salary>2000:
    money_earned=(salary*4)/100
    new_salary=money_earned+salary
    percentage=4
	
print("Novo salario: %.2f"%new_salary)
print("Reajuste ganho: %.2f"%money_earned)
print("Em percentual: {} %".format(percentage))
