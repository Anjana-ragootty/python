s_area=lambda a:a*a
r_area=lambda l,b:l*b
t_area=lambda b,h:0.5*b*h
a=int(input("Enter the sides of squre:"))
print("Area of squre is :",s_area(a))

l=int(input("Enter the length of rectangle:"))
b=int(input("Enter the breadth of rectangle:"))
print("Area of rectangle is :",r_area(l,b))

b=int(input("Enter the base of the triangle:"))
h=int(input("Enter the height of the triangle:"))
print("Area of triangle is :",t_area(b,h))