data={"A":2500, "B":2000, "C":1750, "D":1250, "OUTRA":750}
x=(input("Type your category: ")).upper()
if x in data.keys():
    print(data[x])
else:
    print("no such categoty")