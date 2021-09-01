
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

#| Ex. 4.1 จากเว็บ https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
#| ให้เขียนโปรแกรมที่พา robot ไปที่ธง โดยใช้แค่ move() และ turn_left()

#| Ex. 4.2 จากไฟล์ 4.2.1 Reeborg's World Hurdles 2 Challenge
#|         เขียนโปรแกรมให้ robot ให้วิ่งถึงธง ซึ่งธงจะ random แสดง
#|         มีฟังก์ชัน at_goal() เพิ่มให้ใช้

#| Ex. 4.ุ3 จากไฟล์ 4.2.2 Reeborg's World Hurdles 3 Challenge
#|         เขียนโปรแกรมให้ robot ให้วิ่งถึงธง ซึ่งธงจะ random แสดง
#|         มีฟังก์ชัน front_is_clear() และ wall_in_front เพิ่มให้ใช้

#| Ex. 4.ุ4 จากไฟล์ 4.2.3 Reeborg's World Hurdles 4 Challenge
#|         เขียนโปรแกรมให้ robot ให้วิ่งถึงธง ซึ่งธงจะ random แสดง
#|         มีฟังก์ชัน wall_on_right() และ right_is_clear เพิ่มให้ใช้

#| Ex. 4.5 จากไฟล์ 4.2.4 Reeborg's World Maze Challenge
#|         เขียนโปรแกรมให้ robot ให้วิ่งถึงธง ใน maze 