col1=[]
n1=int(input("Enter a number of color in list 1:"))
for i in range(n1):
    ele=input("Enter a color :")
    col1.append(ele)
col2=[]
n2=int(input("Enter a number of color in list 2:"))
for i in range(n2):
    ele=input("Enter a color :")
    col2.append(ele)
print("List1=",col1)
print("List 2=",col2)
print("The colour is :")
for i in range(len(col1)):
    if col1[i] not in col2:
        print(col1[i])