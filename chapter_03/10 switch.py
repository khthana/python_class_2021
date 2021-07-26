'''
ใน python ไม่มี switch case เหมือนภาษา C
แต่ใน python 3.10 จะมี match case (ตอนนี้เป็น 3.9 จึงยังไม่มี)
เราสามารถใช้ def ประยุกต์ใช้ได้
'''

def switch(choice):
    case = {
        0: "zero",
        1: "one",
        2: "two"}

    return case.get(choice, "nothing")

print(switch(0))
print(switch(1))
print(switch(2))
print(switch(3)) 

