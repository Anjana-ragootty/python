n=int(input("Enter the number of integers in the list 1:"))
print("Enter the intergers in list 1")
lst1=[]
c=1
for i in range(0,n):
    ele=int(input())
    lst1.append(ele)
print("List 1 : ",lst1)
n=int(input("Enter the number of integers in the list 2:"))
print("Enter the intergers in list 2")
lst2=[]
c=1
for i in range(0,n):
    ele=int(input())
    lst2.append(ele)
print("List 2 : ",lst2)
print()
if(len(lst1)==len(lst2)):
    print("The both list have length")
else:
    print("The both list not same length")
s1=0
s2=0
for i in lst1:
    s1=s1+i
for i in lst2:
    s2=s2+i
if(s1==s2):
    print("The both list sum  are equal")
else:
    print("The both list sum are not equal")
for i in lst1:
    for j in lst2:
        if(i==j):
            print(j,end=" ")
print(" have both string")