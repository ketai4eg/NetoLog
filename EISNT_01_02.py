def name(name:str)->str:
    while len(name)<3:
        name=input("Name should have at leat 3 characters, repeat please: ")
    return name

def age_f(age:int)->int:
    while age>100 or age<0:
        age=int(input("Age should be from 0 to 100, repaet please: "))
    return age

def salary(num:int)->int:
    while num<=0:
        num=int(input("Salary should be more than 0, try again: "))
    return num

def sex(s:str)->str:
    while s.lower() not in ["f", "m"]:
        s=input("There is no more genders, only f or m, try again: ")
    return s.lower()

def esciv(data:str)->str:
    while data.lower() not in ["s", "c", "v", "d"]:
        data=input("""You can choose between: 
        s - solteiro
        c - casado
        v - viuvo
        d - divorciado
try again: """)
    return data

def main():
    data=[]
    data.append(name(input("Type your name: ")))
    data.append(age_f(int(input("Your age: "))))
    data.append(salary(int(input("Your salary: "))))
    data.append(sex(input("Your gender: ")))
    data.append(esciv(input("Your status: ")))
    print(data)

main()