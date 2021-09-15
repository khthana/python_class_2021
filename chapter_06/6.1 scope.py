#------------------------------------
# เมื่อมีการใช้ function ปัญหาหนึ่งอาจเกิดขึ้น คือ
# Scope
#---------------------------------------

#| Example 1: Single Definition

x = 'global'
def f():
    def g():
        print(x)
    g()

f()

#| Example 2: Double Definition

x = 'global'
def f():
    x = 'enclosing'

    def g():
        print(x)

    g()

f()

#| Example 3: Triple Definition

x = 'global'
def f():
    x = 'enclosing'
    def g():
        x = 'local'
        print(x)
    g()
f()

#| Example 4: No Definition

def f():
    def g():
        print(x)
    g()
f()

#|LEGB
#|    Local:     ถ้าตัวแปร x อยู่ภายใน function โปรแกรม python จะใช้ตัวแปรใน
#|               function (local)
#|    Enclosing: ถ้าตัวแปร x ไม่อยู่ใน local scope แต่พบใน function ที่อยู่ใน
#|               function ด้านนอก,โปรแกรม python จะใช้ในตัวแปรใน
#|               enclosing function’s scope.
#|    Global:    ถ้าตัวแปร x ไม่อยู่ทั้งใน local scope และ enclosing function’s scope
#|               โปรแกรม python จะค้นหาใน global เป็นลำดับต่อไป
#|    Built-in:  ถ้าไม่พบตัวแปร x ในที่ใดๆ โปรแกรม python จะพยายามหาใน built-in scope

#| Example 5: Local และ Enclosing Name Space

def f():
    print('Start f()')
    def g():
        print('Start g()')
        print('End g()')
        return
    g()
    print('End f()')
    return

f()

#| Example 6: ขอบเขตของตัวแปรแบบ local 

def square(base):
    result = base ** 2
    print(f'The square of {base} is: {result}')
square(10)

#| Example 7: ขอบเขตของตัวแปรแบบ local 

def cube(base):
    result = base ** 3
    print(f'The cube of {base} is: {result}')
cube(30)

#| Example 8: หากแก้ไขตัวแปรแบบ Global ใน function จะเกิดอะไรขึ้น 
var = 100  # A global variable
def increment():
    var = var + 1  # Try to update a global variable
increment()

#| Example 9: กรณีกำหนดตัวแปร Local แล้วอ้างถึง
var = 100  # A global variable
def func():
    print(var)  # Reference the global variable, var
    var = 200   # Define a new local variable using the same name, var
func()

#| Example 10: การอ้างถึงตัวแปร Global ภายใน function
counter = 0  # A global name
def update_counter():
    counter = counter + 1  # Fail trying to update counter
update_counter()


counter = 0  # A global name
def update_counter():
    global counter  # Declare counter as global
    counter = counter + 1  # Successfully update the counter
update_counter()
print (counter)
update_counter()
print (counter)
update_counter()
print (counter)

#| Example 11: การแก้ไขตัวแปร Global โดยใช้การส่งค่าและ return จาก function
global_counter = 0  # A global name
def update_counter(counter):
    return counter + 1  # Rely on a local name
global_counter = update_counter(global_counter)
print (global_counter)
global_counter = update_counter(global_counter)
print (global_counter)
global_counter = update_counter(global_counter)
print (global_counter)

#| Example 12: การสร้างตัวแปร Global จากภายใน function
def create_lazy_name():
    global lazy  # Create a global name, lazy
    lazy = 100
    return lazy
create_lazy_name()
lazy  # The name is now available in the global scope

#| Example 13: การแก้ไขตัวแปร Enclosing โดยใช้คำสั่ง nonlocal 
def func():
    var = 100  # A nonlocal variable
    def nested():
        nonlocal var  # Declare var as nonlocal
        var += 100
    nested()
    print(var)
func()

#| Example 14: แสดงการส่งกลับเป็น function ภายใน ซึ่งเป็น local function

def power_factory(exp):
    def power(base):
        return base ** exp
    return power
square = power_factory(2)
print(square(10))

cube = power_factory(3)
print(cube(10))

cube(5)
print(square(15))

#| Example 15: แสดงการส่งกลับเป็น function ภายใน ซึ่งเป็น local function 
#| แสดงให้เห็นว่า number เป็น free variable สามารถเข้าถึงได้ในทุกระดับ 
#| จะเห็นว่ากรณีนี้ จะมีการเก็บข้อมูล sample เอาไว้ด้วย
#| ซึ่งอาจทำให้สิ้นเปลืองหน่วยความจำ

def mean():
    sample = []
    def _mean(number):
        sample.append(number)
        return sum(sample) / len(sample)
    return _mean
current_mean = mean()
print(current_mean(10))

print(current_mean(15))

print(current_mean(12))

print(current_mean(11))

print(current_mean(13))

#| Example 16: แสดง version ที่ไม่เก็บข้อมูล list 

def mean():
    total = 0
    length = 0
    def _mean(number):
        nonlocal total, length
        total += number
        length += 1
        return total / length
    return _mean
current_mean = mean()
print(current_mean(10))

print(current_mean(15))

print(current_mean(12))

print(current_mean(11))

print(current_mean(13))


