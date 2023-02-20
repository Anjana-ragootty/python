cy=int(input("Enter the current year :"))
fy=int(input("Enter the current year :"))
print("Future leap years:")
i=cy
for i in range(cy,fy):
    if((i % 4 == 0) or (i % 400 == 0) and (i % 100 != 0)):
        print(i)
