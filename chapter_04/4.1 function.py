#---------------------------------------------------
#* ในการทำงานบางอย่างที่ต้องการทำงานซ้ำๆ เราสามารถสร้างเป็น Function ได้ 
#* Python มี Build in function มากมาย
#* ตัวยอย่างของ Build in function
#---------------------------------------------------
print('abc')
len('abc')

#---------------------------------------------------
#* แต่เราก็สามารถสร้าง User defined function ขึ้นใช้เองได้
#? def function_name(parameters):
#?      docstring
#?      statement(s)
#?      return x
#---------------------------------------------------

def hello(name):
    # code ที่อยู่ใน function ต้อง indent 
    """
    Function to print ส่วนนี้เรียกว่า docstring เอาไว้อธิบายการทำงานของ function
    """
    print ("Good afternoon, " + name)

hello("John")
hello("Bob")

#---------------------------------------------------
#*ในการส่งค่ากลับ สามารถใช้ return 
#---------------------------------------------------
def is_even(n):
    if (n%2==0):
        return True
    else:
        return False

#*สามารถเขียนได้อีกแบบ 
def is_even(n): return True if n%2==0 else False

#---------------------------------------------------
#* Ex ถ้าจะทำฟังก์ชัน is_ood() ควรเขียนแบบใด
#---------------------------------------------------
def is_odd(n):
        return not(is_even(n))



#| Ex 4.1 จงเขียน Function absolute value

#| Ex 4.2 จงเขียน Function หาจำนวนหัวที่ต้องจ่าย กรณี มา 4 จ่าย 3
#| พารามิเตอร์รับ head, per_head


### แก้ไขฟังก์ชัน เป็นมาเท่าไร จ่ายเท่าไรก็ได้


#| Ex 4.3 จงเขียนโปรแกรมรับค่าตัวเลข และบอกว่าเป็น square number หรือไม่
#|        โดยให้ทำเป็นฟังก์ชัน

def is_square(n):
        return False;
"""
-1 : False
0 : True
4 : True
5 : False
25 : True
"""

#---------------------------------------------------
#* บางกรณีต้องมีการ Return หลายค่า 
#* เช่น จะเขียนโปรแกรมที่ใส่จำนวนเงิน 
#* แล้ว Return มูลค่าสินค้า กับ ภาษีมูลค่าเพิ่ม
#---------------------------------------------------

def price_with_vat(amount):
        vat = amount * 7 / 107  # 107  * 7 /107
        price = amount - vat
        return price, vat

print(price_with_vat(107))
p, v = price_with_vat(214)
print("p = ", p)
print("v = ", v)

#---------------------------------------------------
#* ลองดูโปรแกรมต่อไปนี้
#---------------------------------------------------

def alpha(a, b):
        c = a + b
        print(c)

print(alpha(5, 3))
print(alpha("rain", "bow"))

#* จะเห็นว่าสามารถทำงานได้ทั้ง 2 แบบ เรียกว่า dynamic type