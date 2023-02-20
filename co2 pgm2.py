n1=0
n2=1
limit=int(input("Enter a limit:"))
print("The fibonacci series upto",limit,"terms are: ")
print(n1)
print(n2)
for i in range(limit-2):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3)