n=int(input("Enter the number of integers in the list:"))
print("Enter the intergers in list")
lst=[]
for i in range(n):
    ele=int(input())
    lst.append(ele)
print("List  : ",lst)
lst1=[]
lst1 = [x for x in lst if x > 0 ]
print("List of +ve integers  : ",lst1)

N=int(input("Enter the number:"))
lst2=[i*i for i in range(1,N+1)]
print("Squre of numbers  : ",lst2)

s=input("Enter a string:")
v=['a','e','i','o','u','A','E','I','O','U']
lst3 = [j for j in s if j in v]
print("vowels in string  : ",lst3)

w=input("Enter a word:")
lst4=[ord(k) for k in w]
print("Ordinal values of word  : ", lst4)