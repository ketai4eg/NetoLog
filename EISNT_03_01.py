x=int(input("Please enter the mark: "))
while x<0 or x>20:
    print("The mark is not correct, please try again: ")
    x = int(input("Please enter the mark: "))
print(x)