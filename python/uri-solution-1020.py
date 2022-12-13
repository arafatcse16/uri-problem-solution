days = int(input())
year = days//365
days %= 365
months =days//30
days -=months*30
print("{} ano(s)".format(year))
print("{} mes(es)".format(months))
print("{} dia(s)".format(days))
