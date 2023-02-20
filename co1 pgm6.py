n=int(input("Enter the number of 1st names in the list:"))
print("Enter the 1st names")
lst=[]
c=0
co=0
for i in range(n):
    ele=input()
    lst.append(ele)
print(lst)

for j in lst:
    for k in j:
        c = j.count('a')
    co=c+co
print("Number of (a) in the list is : " , co)