def menu():
    print("#" *20)
    print("#    หาพื้นที่         #")
    print("#" *20)
    print("# 1. สามเหลี่ยม       #")
    print("# 2. สี่เหลี่ยม         #")
    print("# 3. วงกลม         #")
    print("# 4. ออกจากโปรแกรม    #")
    print("#" *20)

def clear(): print("\n" *10) 

menu()
INPUT = int(input("Enter your choice: "))
while INPUT != 4:
    if INPUT == 1:
        pass
    elif INPUT == 2:
        pass
    elif INPUT == 3:
        pass
    else:
        print("Your choice is wrong!")
    clear()
    menu()
    INPUT = int(input("Enter your choice: "))
else:
    print("Program exit")

 
