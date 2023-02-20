String=input("Enter the string:")
count=0
for i in range(len(String)):
    if String[i]!=' ':
        count=count+1
print("The total number of characters in the string is ",count)