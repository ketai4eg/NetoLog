boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
boys.sort()
girls.sort()
if len(boys)!=len(girls):
    print("some one will stay alone")
else:
    print("Идеальные пары:")
    for b, g in zip(boys,girls):
        print(f'{b} and {g}')