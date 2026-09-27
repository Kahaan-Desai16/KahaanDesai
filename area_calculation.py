def square():
    a=int(input("enter the side of the square you want to calculate"))
    area=a*a
    return area
def rectangle():
    l=int(input("enter the length"))
    b=int(input("enter the breadth"))
    area=l*b
    return area
def circle():
    r=int(input("enter the radius"))
    area=3.14*r*r
    return area
def triangle():
    a=int(input("enter the length of perpendicular"))
    b=int(input("enter the length of base"))
    area=0.5*a*b
    return area
ans='y'
while ans=='y':
    print("WELCOME")
    print("please make a choice from the below listed shapes")
    print("1.square")
    print("2.rectangle")
    print("3.circle")
    print("4.triangle")
    a=int(input("enter the number of your choice"))
    if a==1:
        x=square()
        print("the area of the shape is :",x)
    elif a==2:
        x=rectangle()
        print("the area of the shape is :",x)
    elif a==3:
        x=circle()
        print("the area of the shape is :",x)
    elif a==4:
        x=triangle()
        print("the area of the shape is :",x)
    ans=input("do you want to continue?(y/n)")
print("thank you")

    
    
