("Hello!")
x=0
while x==0:
    print("[1] Calculate the area of a rectangle")
    print("[2] Calculate the perimeter of a rectangle")
    print("[3] Calculate the area of a circle")
    print("[4] Calculate the perimeter of a cirlce")
    print("[5] Exit\n")
    decision=int(input("What you want to do? "))
    pi=3.14
    if decision==1:
        print("\n[1] Calculate the area of a rectangle")
        print("Enter data:")
        a=int(input("A side: "))
        b=int(input("B side: "))
        RectangleArea=a*b
        print("Rectangle, with A side",a,"and B side",b,"has area equall",RectangleArea)
        yyy=input("Click any button to come back to menu\n")
        x=0
    elif decision==2:
        print("\n[2] Calculate the perimeter of a rectangle")
        print("Enter data:")
        a=int(input("A side: "))
        b=int(input("B side: "))
        RectanglePerimeter=2*a+2*b
        print("Rectangle, with A side",a,"and B side",b,"has perimeter equall",RectanglePerimeter)
        yyy=input("Click any button to come back to menu\n")
        x=0
    elif decision==3:
        print("\n[3] Calculate the area of a circle")
        r=int(input("Enter length radian: "))
        CircleArea=pi*(r*r)
        print("Area of a circle with radian length",r,"is equal",CircleArea)
        yyy=input("Click any button to come back to menu\n")
        x=0
    elif decision==4:
        print("\n[4] Calculate the perimeter of a cirlce")
        r=int(input("Enter length radian: "))
        CirclePerimeter=2*pi*r
        print("Perimeter of a circle with radian length",r,"is equal",CirclePerimeter)
        yyy=input("Click any button to come back to menu\n")
        x=0
    elif decision==5:
        print("[5] Exit")
        yyy=input("Click any button to continuous..\n")
        x=1
    else:
        print("Unknown decision. Go to menu and choose 1-5 options!\n")
        x=0
