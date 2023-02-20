list = []
for x in range(7):
    x = int(input("enter an integer value :"))
    if(x<100):
        list.append(x)
    else:
        list.append("over")
print(list)
