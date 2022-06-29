queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]
result={}
summ=0
for items in queries:
    summ+=1
    line=items.split(" ")
    result.setdefault(len(line),int())
    result[len(line)]+=1
for w_num, count in result.items():
    print(f"{w_num} words were asked in {(count/summ):.0%}")