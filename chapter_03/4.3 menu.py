def menu():
    print("#" *20)
    print("#    หาพื้นที่         #")
    print("#" *20)
    print("# 1. สามเหลี่ยม       #")
    print("# 2. สี่เหลี่ยม         #")
    print("# 3. วงกลม         #")
    print("# 4. ออกจากโปรแกรม    #")
    print("#" *20)

def Triangle(height, base):
    return 0.5 * height * base

def Rectangle(width, length):
    return width * length

def Circle(radius):
    return 3.14 * (radius ** 2)

def clear(): print("\n" *10) 

menu()
INPUT = int(input("Enter your choice: "))
while INPUT != 4:
    if INPUT == 1:
        height = float(input("Enter height = "))
        base = float(input("Enter base = "))
        print("Triangle area = ", Triangle(height, base))
    elif INPUT == 2:
        width = float(input("Enter width = "))
        length = float(input("Enter length = "))
        print("Rectangle area = ", Rectangle(width, length))
    elif INPUT == 3:
        radius = float(input("Enter radius = "))
        print("Circle area = ", Circle(radius))
    else:
        print("Your choice is wrong!")
    clear()
    menu()
    INPUT = int(input("Enter your choice: "))
else:
    print("Program exit")

 
