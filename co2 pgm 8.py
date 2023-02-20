n=int(input("Enter the number of words:"))
list=[]
for i in range(n):
    r=(input("Enter the word:"))
    list.append(r)
print(list)
max=(len(list[0]))
temp=list[0]
for i in list:
    if(len(i)>max):
        max=len(i)
        temp=i
print("The word having longest length is : ",temp," and its length is : ",max)
