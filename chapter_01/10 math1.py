"""
*Python math operation
a + b
a – b
a * b
b / a
b % a Modulus
a**b  Exponent
9//2 = 4 Floor Division

* หากมีวงเล็บ ต้องทำในวงเล็บก่อน
* หากไม่มีวงเล็บ จะทำตามลำดับดังนี้
* ยกกำลัง** , / , // , % จากนั้นจึงเป็น + -
"""
a = 0.2
b = 0.1
print(a + b)

#* คำนวณปริมาตรของ 4 เหลี่ยมลูกบาศก์
width = float(input("Enter input width = "))
length = float(input("Enter input length = "))
height = float(input("Enter input height = "))

print("Volume of Cube : ", width * height * length)

#%%
Income = float(input("Enter your income (Baht): "))
VAT = float(input("Enter your VAT (%): "))
Tax = (Income * VAT) / 100
print("Your Tax is ", Tax, "Baht")

# ====================================================
#* พื้นที่สามเหลี่ยม

High = 12.0
Base = 9.0
TriangleArea = 0.5 * High * Base
print("TriangleArea =", TriangleArea, "cm")

"""
* เปลี่ยนเขียนโปรแกรมค่าจากองศาเซลเซียสไปเป็นองศาฟาเรนไฮต์
* สูตรในการเปลี่ยนค่าจากองศาเซลเซียสไปเป็นองศาฟาเรนไฮต์มีดังนี้
* F = (9/5)*C+32
* รับข้อมูลองศาเซลเซียสเป็นจำนวนจริง
* แสดงผลตัวเลขจำนวนจริง เป็นองศาฟาเรนไฮต์
* 39.85 -> 103.73
"""

#* โปรแกรมพื้นที่สามเหลี่ยมให้รับ Input
# ====================================================

#* โปรแกรมหาเศษคละ
a = int(input("Enter input a = "))
b = int(input("Enter input b = "))
x = a // b
y = a % b
print("เศษคละเท่ากับ ", x, "(", y, "/", b, ")")

#* ----------------------------------------------------
#* คำนวณจำนวนเงินที่ขาดทุน เมื่อซื้อส้มมาขายในราคาต่ำกว่า

a = int(input("Enter the amount of oranges purchased (kiilo) = "))
b = int(input("Enter the price of the purchased orange per a kilogram (Baht) = "))
c = int(input("Enter the price of the orange sold (Baht) = "))
loss = (a * b) - (a * c)
result = (loss * 100) / (a * b)
print("ขายขาดทุน =", result, "%")

#| จงเขียนโปรแกรมหาปริมาตร ทรงกรวย

"""
| จงเขียนโปรแกรมคำนวณ หาคำตอบของสมการ
| ax2 + bx +c = 0
| https://krupraiwan.wordpress.com/2014/09/15/quadratic-by-formula/
| รับค่า a,b,c แล้วให้คำตอบค่า x
| hint การทำ square root ใช้ ยกกำลัง 0.5
"""

#! เขียนโปรแกรมคำนวณหลักสุดท้ายของบัตรประชาชน

