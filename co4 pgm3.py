class Rectangle:
    def __init__(self,length,width):
        self.__length=length
        self.__width=width
    def area(self):
        return (self.__length * self.__width)
    def __lt__(self,other):
        return self.area<other.area
r1=Rectangle(4,4)
r2=Rectangle(5,7)
ar1=r1.area()
print("1st Rectangle area =",ar1)
ar2=r2.area()
print("2nd Rectangle area =",ar2)
if(ar1<ar2):
    print("The 1st rectangle area lessthan 2nd rectangle")
else:
    print("The 2nd rectangle area lessthan 1st rectangle")
