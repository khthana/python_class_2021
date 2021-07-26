def menu():
    print("#" *20)
    print("#  Volume calculation program   #")
    print("#" *20)
    print("# 1. Prism           #")
    print("# 2. Cylinder        #")
    print("# 3. Cone            #")
    print("# 4. Sphere          #")
    print("# 5. Exit            #")
    print("#" *20)

def Prism(width, length, height):
    return width * length * height

def Cylinder(r, height):
    return (22/7) * (r * r) * height

def Cone(r, height):
    return (1/3) * (22/7) * (r * r) * height

def Sphere(r):
    return (4/3) * (22/7) * (r ** 3)

def clear(): print("\n" *10) 

menu()
INPUT = int(input("Enter your choice: "))
while INPUT != 5:
    if INPUT == 1:
        width = float(input("Enter width = "))
        length = float(input("Enter length = "))
        height = float(input("Enter height = "))
        print("Prism volume = %0.2f" %Prism(width, length, height))
    elif INPUT == 2:
        r = float(input("Enter radius = "))
        height = float(input("Enter height = "))
        print("Cylinder volume = %0.2f" %Cylinder(r, height))
    elif INPUT == 3:
        r = float(input("Enter radius = "))
        height = float(input("Enter height = "))
        print("Cone volume = %0.2f" %Cone(r, height))
    elif INPUT == 4:
        r = float(input("Enter radius = "))
        print("Sphere volume = %0.2f" %Sphere(r))
    else:
        print("Your choice is wrong!")
    clear()
    menu()
    INPUT = int(input("Enter your choice: "))
else:
    print("Program exit")

  
