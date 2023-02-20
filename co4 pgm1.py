class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        ar=self.length * self.breadth
        print("Area of Rectangle=",ar)
        return ar
    def perimeter(self):
        peri= 2*(self.length+self.breadth)
        print("Perimeter of Rectangle=",peri)
    def Compare(self,other):
        print("\nCompare two object :\n")
        if self.area() > other.area():
            print("The 1st object area greater than 2nd object")
        else:
            print("The 2nd object area greater than  1st object")
print("OBJECT 1")
r1=Rectangle(5,6)
r1.area()
r1.perimeter()
print("OBJECT 2")
r2=Rectangle(4,8)
r2.area()
r2.perimeter()
r1.Compare(r2)