def octa(num):
    return str(oct(num))[2:]

def hexa(num):
    return (str(hex(num))[2:]).upper()

def bina(num):
    return str(bin(num))[2:]

def spaces(symbol):

    return len(str(symbol))-2
def print_formatted(number:int)->None:
    max_len = len(bin(number)) - 2
    for i in range(1,number+1):
        print(f"{' '*(max_len-len(str(i)))}{i} {' '*(max_len-spaces(oct(i)))}{octa(i)} {' '*(max_len-spaces(hex(i)))}{hexa(i)} {' '*(max_len-spaces(bin(i)))}{bina(i)}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)